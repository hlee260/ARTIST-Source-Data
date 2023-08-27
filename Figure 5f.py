# Import packages
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import pandas as pd


# Function for the comparator based on Eqns S6, S7, S8
def Comparator(y, t, k_txn, k_th, k_sd, Ref_dART, IFN_dART, Reporter0):
    Ref_RNA, IFN_RNA, Reporter_reacted = y
    dRef_RNAdt = k_txn*Ref_dART - k_th*Ref_RNA*IFN_RNA - k_sd*Ref_RNA*Reporter0 + k_sd*Ref_RNA*Reporter_reacted
    dIFN_RNAdt = k_txn*IFN_dART - k_th*Ref_RNA*IFN_RNA
    dReporter_reacteddt = k_sd*Ref_RNA*Reporter0 - k_sd*Ref_RNA*Reporter_reacted
    return [dRef_RNAdt, dIFN_RNAdt, dReporter_reacteddt]


# Initial conditions
Ref_RNA0 = 0 # Initial Ref-O1-RNA concentration
IFN_RNA0 = 0 # Initial IFN-O1'-RNA concentration
Reporter_reacted0 = 0.0 # Initial Reacted reporter concentration
y0 = [Ref_RNA0, IFN_RNA0, Reporter_reacted0]
k_txn = 0.004 * 60 # Fitted transcription rate constant
k_th = 1e6/1e9 * 60 # RNA:RNA hybridization rate constant
k_sd = 1e5/1e9 * 60 # Strand displacement rate constant based on 6 bp toehold
Reporter0 = 250 # Initial Reporter concentration
IFN_dART_0 = 50 # Initial IFN-O1'-dART concentration

Ref_dART_list = [15, 25, 40] # List of initial Ref-O1-dART concentrations
IFN_list = [0, 5, 10, 20, 30, 50, 100, 200] # List of varying IFN-γ concentration

# Define a function to calculate unbound IFN-O1'-dART concentration based on Kd,apparent and a list of IFN-γ concentrations
# Based on Eqn S5
def calculate_IFN_dART_unbound(L_0, K_D):
    m = (IFN_dART_0+K_D+L_0) 
    IFN_dART_bound = ((m)-(math.sqrt((m**2)-4*(IFN_dART_0*L_0))))/2
    IFN_dART_unbound = IFN_dART_0 - IFN_dART_bound
    return IFN_dART_unbound

# Create an empty list to store simulated IFN_dART_unbound concentrations for each IFN-γ concentration
sim_IFN_dART_unbound_list = []
for IFN in IFN_list:
    # Calculate unbound_dART concentrations based on a Kd value and list of ligand concentrations
    sim_IFN_dART_unbound_list.append(calculate_IFN_dART_unbound(IFN, 8)) # Estimated Kd (dashed line)

# Create an empty list to store the simulated Reporter_reacted values for each IFN_dART_unbound concentration
# This list varies on the concentration of Ref_dART
sim_Reporter_reacted_15Ref_list = []
sim_Reporter_reacted_25Ref_list = []
sim_Reporter_reacted_40Ref_list = []    
    
# Time points to run the simulation
t = np.linspace(0, 240, 1000)

# Calculate reacted reporter kinetics for each concentration of Ref_dART
for IFN_dART in sim_IFN_dART_unbound_list:
    React_rep_15Ref = odeint(Comparator, y0, t, args=(k_txn, k_th, k_sd, Ref_dART_list[0], IFN_dART, Reporter0))
    React_rep_25Ref = odeint(Comparator, y0, t, args=(k_txn, k_th, k_sd, Ref_dART_list[1], IFN_dART, Reporter0))
    React_rep_40Ref = odeint(Comparator, y0, t, args=(k_txn, k_th, k_sd, Ref_dART_list[2], IFN_dART, Reporter0))
    # extract Reporter_reacted concentration for each concentration of Ref_dART
    Reporter_reacted_15Ref = React_rep_15Ref[:, 2]
    Reporter_reacted_25Ref = React_rep_25Ref[:, 2]
    Reporter_reacted_40Ref = React_rep_40Ref[:, 2]
    # Endpoint measurements
    sim_Reporter_reacted_15Ref_list.append(Reporter_reacted_15Ref[-1])
    sim_Reporter_reacted_25Ref_list.append(Reporter_reacted_25Ref[-1])
    sim_Reporter_reacted_40Ref_list.append(Reporter_reacted_40Ref[-1])

# Import experimental data
data = pd.read_excel('Figure 5e.xlsx')
IFN_conc = data.loc[:, 'IFN']
data_plot = data.loc[:, '15 Ref':'40 Ref']

        
# plot the dose-response curve    
lw = 2
plt.plot(IFN_list, sim_Reporter_reacted_15Ref_list, linestyle = '--',  label = 'Simulation', linewidth=lw)
plt.plot(IFN_list, sim_Reporter_reacted_25Ref_list, linestyle = '--', linewidth=lw)
plt.plot(IFN_list, sim_Reporter_reacted_40Ref_list, linestyle = '--', linewidth=lw)
plt.plot(IFN_conc,data_plot['15 Ref'],marker='o', label = 'IFN-O1-C-100', color = [0,0.4,1], markerfacecolor=(0,0.4,1),linewidth=0,markersize=10)
plt.plot(IFN_conc,data_plot['25 Ref'],marker='o', label = 'IFN-O1-C-50', color = [0,0,1],  markerfacecolor=(0,0,1),linewidth=0,markersize=10)
plt.plot(IFN_conc,data_plot['40 Ref'],marker='o', label = 'IFN-O1-C-30', color = [0,0,0.5], markerfacecolor=(0,0,0.5),linewidth=0,markersize=10)


fs = 20
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(25,275)
ax1 = plt.gca()
ax1.set_xscale('log')
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('[IFN-γ] (nM)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(fontsize=fs-4)
# plt.title("IFN-γ", fontsize=fs-1, weight='bold', loc = 'right')

# plt.savefig('Figure 5f.svg')





