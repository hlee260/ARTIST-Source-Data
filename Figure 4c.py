'''Data processing excel with python'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# import numpy as np
data = pd.read_excel('Figure4c.xlsx')
exp_data = data.loc[:,'IFN_RNH1':'TNF_RNH2']

conc = [5, 10, 100, 1000]

fs = 20

plt.plot(conc, exp_data['IFN_RNH1'], marker='o', markerfacecolor='blue',linewidth = 0, markersize=8, label = 'IFN-γ')
plt.plot(conc, exp_data['IFN_RNH2'], marker='o', markerfacecolor='blue',linewidth = 0, markersize=8)
plt.plot(conc, exp_data['Thr_RNH1'], marker='o', markerfacecolor='green',linewidth = 0, markersize=8, label = 'Thrombin')
plt.plot(conc, exp_data['Thr_RNH2'], marker='o', markerfacecolor='green',linewidth = 0, markersize=8)
plt.plot(conc, exp_data['IL6_RNH1'], marker='o', markerfacecolor='purple',linewidth = 0, markersize=8, label = 'IL-6')
plt.plot(conc, exp_data['IL6_RNH2'], marker='o', markerfacecolor='purple',linewidth = 0, markersize=8)
plt.plot(conc, exp_data['TNF_RNH1'], marker='o', markerfacecolor='red',linewidth = 0, markersize=8, label = 'TNF-α')
plt.plot(conc, exp_data['TNF_RNH2'], marker='o', markerfacecolor='red',linewidth = 0, markersize=8)


plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-5,55)
ax2 = plt.gca()
ax2.set_xscale('log')
ax2.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax2.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('[Protein] (nM)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(loc='upper right', fontsize=fs-6)

plt.savefig('Figure 4c.svg')