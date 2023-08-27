import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from brokenaxes import brokenaxes


data = pd.read_excel('Figure 6e.xlsx')
IFN = data.loc[:, 'IFN']
data_plot = data.loc[:,'IFN-O4-1-G1O4':'IFN-O1-C-30']

# Plotting the data

# plt.figure()

lw = 1
fs = 20
plt.figure()

ax1 = plt.gca()

ax1.set_xscale('log')
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,260)
plt.xlabel('[Protein] (nM)',fontsize=fs)



ax1.plot(protein_AMP,data_plot['IFN-O4-1-G1O4'], marker='o', color = (0.5, 0, 0.5), 
         markerfacecolor=(0.5,0,0.5),linewidth=lw,markersize=9, label = 'Amplifier')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-25,275)
plt.xlabel('[IFN-γ] (nM)',fontsize=fs)

ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
ax1.set_ylabel('[Reacted O4 Reporter] (nM)',fontsize=fs, color = 'tab:purple') 
ax1.tick_params(axis='y', labelcolor='tab:purple', labelsize = fs)
# plt.legend(loc='upper left', fontsize=11)

ax2=ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('[Reacted O1 Reporter] (nM)',fontsize=fs, color = 'tab:blue') 
ax2.tick_params(axis='y', labelcolor='tab:blue', labelsize = fs)
ax2.plot(protein_noAMP,data_plot['IFN-O1-C-100'], marker='o', color = (0, 0.6, 1), 
         markerfacecolor=(0,0.6,1),linewidth=lw,markersize=9, label = 'IFN-O1-C-100')
ax2.plot(protein_noAMP,data_plot['IFN-O1-C-50'], marker='o', color = (0, 0, 1), 
         markerfacecolor=(0,0,1),linewidth=lw,markersize=9, label = 'IFN-O1-C-50')
ax2.plot(protein_noAMP,data_plot['IFN-O1-C-30'], marker='o', color = (0, 0, 0.5), 
         markerfacecolor=(0,0,0.5),linewidth=lw,markersize=9, label = 'IFN-O1-C-30')


ax2.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax2.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
ax2.set_ylabel('[Reacted O1 Reporter] (nM)',fontsize=fs, color = 'tab:blue') 
ax2.tick_params(axis='y', labelcolor='tab:blue', labelsize = fs)

ax1.set_xscale('log')
ax2.set_xscale('log')

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-25,275)
plt.xlabel('[IFN-γ] (nM)',fontsize=fs)

plt.legend(loc='upper left', fontsize=11)
# plt.savefig('Figure 6e.svg')