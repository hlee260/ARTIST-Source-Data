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
k_th = 1e6/1e9 * 60 # RNA:RNA hybridization rate constant
k_sd = 1e5/1e9 * 60 # Strand displacement rate constant based on 6 bp toehold
Reporter0 = 250 # Initial Reporter concentration
Ref_dART = 25 # Initial Ref-O1-dART concentration
IFN_dART_0 = 50 # Initial IFN-O1'-dART concentration


k_txn_list = [0.002 * 60, 0.004 * 60, 0.008 * 60] # List of transcription rate constants
IFN_list = [0, 5, 10, 20, 50, 75, 100] # List of varying IFN-γ concentration

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
sim_Reporter_reacted_2UT7_list= []
sim_Reporter_reacted_4UT7_list = []
sim_Reporter_reacted_8UT7_list = []    
    
# Time points to run the simulation
t = np.linspace(0, 240, 1000)

# Calculate reacted reporter kinetics for each concentration of Ref_dART
for IFN_dART in sim_IFN_dART_unbound_list:
    React_rep_2UT7 = odeint(Comparator, y0, t, args=(k_txn_list[0], k_th, k_sd, Ref_dART, IFN_dART, Reporter0))
    React_rep_4UT7 = odeint(Comparator, y0, t, args=(k_txn_list[1], k_th, k_sd, Ref_dART, IFN_dART, Reporter0))
    React_rep_8UT7 = odeint(Comparator, y0, t, args=(k_txn_list[2], k_th, k_sd, Ref_dART, IFN_dART, Reporter0))
    # extract Reporter_reacted concentration for each concentration of Ref_dART
    Reporter_reacted_2UT7 = React_rep_2UT7[:, 2]
    Reporter_reacted_4UT7 = React_rep_4UT7[:, 2]
    Reporter_reacted_8UT7 = React_rep_8UT7[:, 2]
    # Endpoint measurements
    sim_Reporter_reacted_2UT7_list.append(Reporter_reacted_2UT7[-1])
    sim_Reporter_reacted_4UT7_list.append(Reporter_reacted_4UT7[-1])
    sim_Reporter_reacted_8UT7_list.append(Reporter_reacted_8UT7[-1])

# Import experimental data
data = pd.read_excel('Figure S22.xlsx')
IFN_conc = data.loc[:, 'IFN']
data_plot = data.loc[:, '2U':'8U']

# plot the dose-response curve 
lw = 2
plt.plot(IFN_list, sim_Reporter_reacted_2UT7_list, linestyle = '--',  label = '2 U uL-1', linewidth=lw)
plt.plot(IFN_list, sim_Reporter_reacted_4UT7_list, linestyle = '--', label = '4 U uL-1', linewidth=lw)
plt.plot(IFN_list, sim_Reporter_reacted_8UT7_list, linestyle = '--',  label = '8 U uL-1', linewidth=lw)

plt.plot(IFN_conc,data_plot['2U'],marker='o', label = 'Experiment', color = [0,0,1], markerfacecolor=(0,0,1),linewidth=0,markersize=10)
plt.plot(IFN_conc,data_plot['4U'],marker='o',  color = [0,0,1],  markerfacecolor=(0,0,1),linewidth=0,markersize=10)
plt.plot(IFN_conc,data_plot['8U'],marker='o', color = [0,0,1], markerfacecolor=(0,0,1),linewidth=0,markersize=10)

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

# plt.savefig('Figure S22.svg')








