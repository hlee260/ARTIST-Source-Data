import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import experimental data
data = pd.read_excel('Figure 5h.xlsx')
IFN_conc = data.loc[:, 'IFN']
data_plot = data.loc[:, '20K':'100K']


lw = 3
# plt.figure(figsize=(4, 5))

plt.plot(IFN_conc,data_plot['20K'], marker='o',color = (0,0.6,1), markerfacecolor=(0,0.6,1),linewidth=1,markersize=8, label = '20 mM K+')
plt.plot(IFN_conc,data_plot['60K'], marker='o',color = (0,0,1), markerfacecolor=(0,0,1),linewidth=1,markersize=8, label = '60 mM K+')
plt.plot(IFN_conc,data_plot['100K'], marker='o',color = (0,0,0), markerfacecolor=(0,0,0),linewidth=1,markersize=8, label = '100 mM K+')

fs = 20

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(0,300)
# plt.xlim(4,104)
ax2 = plt.gca()
ax2.set_xscale('log')
ax2.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax2.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('[IFN-γ] (nM)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(loc='upper left', fontsize=fs-4)
# plt.savefig('Figure 5h.svg')

'''Code is also used to generate Figure 5j'''