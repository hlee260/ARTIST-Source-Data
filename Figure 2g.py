# Import Packages

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import pandas as pd



# Define function for the ARTIST reaction based on Eqns S1 and S2

def ARTIST_rxn(y, t, k_txn, k_sd, dART, Reporter0):
    RNA, Reporter_reacted = y
    dRNAdt = k_txn*dART - k_sd*RNA*Reporter0 + k_sd*RNA*Reporter_reacted
    dReporter_reacteddt = k_sd*RNA*Reporter0 - k_sd*RNA*Reporter_reacted
    return [dRNAdt, dReporter_reacteddt]


# Initial conditions
RNA0 = 0 # Initial RNA concentration
Reporter_reacted0 = 0.0 #Initial reacted reporter concentration
dART_0 = 10 # Change initial dART concentration here.
k_txn = 0.0015 * 60 # Txn rate constant (fitted)
k_sd = 1e5/1e9 * 60 # Strand displacement rate constant based on 6 bp toehold
Reporter0 = 100 # Initial reporter concentration
t = np.linspace(0, 120, 1000) # Time interval of the reaction between 0 and 120 minutes.
L_0_list = np.arange(-1, 10000) # Initial ligand concentrations
y0 = [RNA0, Reporter_reacted0] # Initial RNA and reacted reporter concentrations as y0

# Define a function to calculate unbound dART concentration based on a Kd and a range of protein ligand concentrations
# Based on Eqn S5
def calculate_unbound_dART(L_0, K_D):
    m = (dART_0+K_D+L_0) 
    dART_bound = ((m)-(math.sqrt((m**2)-4*(dART_0*L_0))))/2
    unbound_dART_conc = dART_0 - dART_bound
    return unbound_dART_conc

sim_unbound_dART_list = []
sim_unbound_dART_list_upper = []
sim_unbound_dART_list_lower = []

for j in (L_0_list):
    # Calculate unbound_dART concentrations based on a Kd value and list of ligand concentrations
    sim_unbound_dART_list.append(calculate_unbound_dART(L_0_list[j], 8)) # Estimated Kd (dashed line)
    
    # We can also calculate unbound_dART concentrations based on upper or lower bound Kds
    sim_unbound_dART_list_upper.append(calculate_unbound_dART(L_0_list[j], 20)) # Upper Kd
    sim_unbound_dART_list_lower.append(calculate_unbound_dART(L_0_list[j], 1)) # Lower Kd

# create an empty list to store the simulated Reporter_reacted values for each unbound_dART concentration
sim_Reporter_reacted_list = []

# Simulated Reporter_reacted values for each dART based on Upper or lower bound Kd's: 
sim_Reporter_reacted_list_upper = []
sim_Reporter_reacted_list_lower = []

# Simulation for each value of unbound_dART based on estimated Kd
for dART_unbound in sim_unbound_dART_list:
    React_rep = odeint(ARTIST_rxn, y0, t, args=(k_txn, k_sd, dART_unbound, Reporter0))
    # extract the Reporter_reacted concentrations from the solution
    Reporter_reacted = React_rep[:, 1]
    sim_Reporter_reacted_list.append(Reporter_reacted[-1])

'''Reacted reporter kinetics of 10 nM dART for 0 to 1000 IFN-γ'''

lw = 2
fs = 20


# initial conditions
L_2g_list = [0, 5, 10, 100, 1000]

sim2g_unbound_dART_list = []

for L in L_2g_list:
    # Calculate unbound_dART concentrations based on a Kd value and list of ligand concentrations
    sim2g_unbound_dART_list.append(calculate_unbound_dART(L, 8)) # Estimated Kd (dashed line)

# Simulate ARTIST rxn for each unbound dART concentration
for dART_unbound in sim2g_unbound_dART_list:
    # Simulate reacted reporter concentration for each unbound dART concentration
    React_rep = odeint(ARTIST_rxn, y0, t, args=(k_txn, k_sd, dART_unbound, Reporter0))
    Reporter_reacted = React_rep[:, 1]
    # plot the kinetic results
    plt.plot(t, Reporter_reacted, linestyle = '--',  label = '0 nM', linewidth=lw)

#Import experimental data
datafile = pd.read_excel('Figure2g.xlsx')
time = datafile['Time']
data = datafile.loc[:, '0 nM':'1000 nM']
time = time - time[0]

plt.plot(time, data['0 nM'], label = '0 nM', color=[0,0,0.2],linewidth=lw)
plt.plot(time, data['5 nM'], label = '5 nM', color=[0,0,0.5], linewidth=lw)
plt.plot(time, data['10 nM'], label = '10 nM', color=[0,0,0.8], linewidth=lw)
plt.plot(time, data['100 nM'], label = '100 nM', color=[0,0,1], linewidth=lw)
plt.plot(time, data['1000 nM'],label = '1000 nM', color=[0,0.5,1], linewidth=lw)


plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(["0 nM", "5 nM", "10 nM", "100 nM", "1000 nM"], loc='upper left', fontsize=11)

# plt.savefig('Figure 2g.svg')
