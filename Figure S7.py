'''Function to plot kinetic plot of 10 nM dART for 0-1000 IFN'''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import pandas as pd


datafile = pd.read_excel('Figure S7.xlsx')
time = datafile['Time']
data = datafile.loc[:, 'avg':'max']
time = time - time[0]

def ARTIST_txn(y, t, k_txn, k_sd, dART, Reporter0):
    RNA, Reporter_reacted = y
    dRNAdt = k_txn*dART - k_sd*RNA*Reporter0 + k_sd*RNA*Reporter_reacted
    dReporter_reacteddt = k_sd*RNA*Reporter0 - k_sd*RNA*Reporter_reacted
    return [dRNAdt, dReporter_reacteddt]

# initial conditions
RNA0 = 0
Reporter_reacted0 = 0.0
y0 = [RNA0, Reporter_reacted0]

# parameters
k_txn = 0.0015 * 60
k_sd = 1e4/1e9 * 60
Reporter0 = 100

dART_list = [10.0]
lw = 3

# time points to solve the system of ODEs at
t = np.linspace(0, 120, 1000)

# solve the system of ODEs for each value of dART
for dART in dART_list:
    # initial conditions
    
    # solve the system of ODEs
    React_rep = odeint(ARTIST_txn, y0, t, args=(k_txn, k_sd, dART, Reporter0))
    
    # extract the RNA and Reporter_reacted concentrations from the solution
    RNA = React_rep[:, 0]
    Reporter_reacted = React_rep[:, 1]
    
    # plot the results
    plt.plot(t, Reporter_reacted, color=[1,0,0], linestyle = '--',  label = 'Simulation', linewidth=lw-1)


# Experimental results

plt.plot(time, data['avg'], label = 'Experiment', color=[0,0,0.2],linewidth=lw-1)
#Min and max plots
plt.plot(time, data['min'], color=[0,0,0], linewidth=lw-3)
plt.plot(time, data['max'], color=[0,0,0], linewidth=lw-3)
#Shades
plt.fill_between(time, data['min'], data['max'], color=[0,0,0.2], alpha=0.3, interpolate=True)

fs = 20

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(loc='upper left', fontsize=fs-4)

# plt.savefig('Figure S7.svg')



