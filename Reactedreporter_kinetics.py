'''Data processing Comparator with protein'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel('Figure5d.xlsx')

time = data['Time']
data_plot = data.loc[:, '0 nM':'100 nM']
time = time - time[0]

lw = 3
fs = 20

plt.plot(time,data_plot['0 nM'],color=(0,1,1),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['5 nM'],color=(0,0.8,1),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['10 nM'],color=(0,0.4,1),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['20 nM'],color=(0,0,1),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['50 nM'],color=(0,0,0.6),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['75 nM'],color=(0,0,0.4),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['100 nM'],color=(0,0,0.2),linewidth=lw,linestyle='-')

# Customize graph

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-25,275)
plt.xlim(0,240)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(['0 nM','5 nM', '10 nM','20 nM','50 nM','75 nM', '100 nM'], fontsize=fs-6)
# plt.savefig('Figure 5d.svg')    



