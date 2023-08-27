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

# Simulation for each value of unbound_dART based on estimated upper bound Kd    
for dART_unbound in sim_unbound_dART_list_upper:
    React_rep_upper = odeint(ARTIST_rxn, y0, t, args=(k_txn, k_sd, dART_unbound, Reporter0))
    # extract the Reporter_reacted concentrations from the solution
    Reporter_reacted_upper = React_rep_upper[:, 1]
    sim_Reporter_reacted_list_upper.append(Reporter_reacted_upper[-1])
    
# Simulation for each value of unbound_dART based on estimated lower bound Kd    
for dART_unbound in sim_unbound_dART_list_lower:
    React_rep_lower = odeint(ARTIST_rxn, y0, t, args=(k_txn, k_sd, dART_unbound, Reporter0))
    # extract the Reporter_reacted concentrations from the solution
    Reporter_reacted_lower = React_rep_lower[:, 1]
    sim_Reporter_reacted_list_lower.append(Reporter_reacted_lower[-1])
    

# Plotting the dose-response curve using matplotlib
lw =2
fs =20

fig, ax1 = plt.subplots()

# plot the simulated dose-response curve
plt.plot(L_0_list, sim_Reporter_reacted_list, color='orange', linestyle = '--', label = 'Simulation', linewidth=lw) 

# Shade for Upper/lower bound Kds
plt.fill_between(L_0_list, sim_Reporter_reacted_list_upper,  sim_Reporter_reacted_list_lower, color='orange', alpha=0.2, interpolate=True)

# We can plot the simulation with experiments

datafile = pd.read_excel('Figure2f_EPM.xlsx')
concentrations = datafile['IFN']
EPM = datafile.loc[:, 'Average':'Replicate 3']
plt.plot(concentrations, EPM['Average'], 'o', linewidth = 4, markersize = 10, color = 'blue', label = 'Experiment')
plt.plot(concentrations, EPM['Replicate_1'], 'o', linewidth = 0, markersize = 5, color = [0,0,0.5])
plt.plot(concentrations, EPM['Replicate_2'], 'o', linewidth = 0, markersize = 5, color = [0,0,0.5])
plt.plot(concentrations, EPM['Replicate_3'], 'o', linewidth = 0, markersize = 5, color = [0,0,0.5])



# Display and save graph
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.ylim(-10,110)

ax1.set_xscale('log')
ax1.set_xlabel('[IFN-γ] (nM)', fontsize = fs)
ax1.set_ylabel('[Reacted Reporter] (nM)', fontsize = fs)
plt.legend(fontsize = fs-4)
# plt.savefig('Figure 2f.svg')
plt.show()