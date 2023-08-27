'''Data processing Comparator with just templates'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel('Figure6c.xlsx')
time = data['Time']
data_plot = data.loc[:, '0 nM':'50 nM']
time = time - time[0]

lw = 3
fs = 20

plt.plot(time,data_plot['0 nM'],color=(0,0,0),linewidth=lw,linestyle='-')
plt.plot(time,data_plot['50 nM'],color=(0,0,1),linewidth=lw,linestyle='-')

# Customize graph

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-25,275)
plt.xlim(0,120)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.legend(['0 nM','50 nM'], loc='upper left', fontsize = fs-4)
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('[Reacted O4 Reporter] (nM)',fontsize=fs)
plt.savefig('Figure 6c.svg')    
plt.figure()

'''Code is also used to plot Figure S27'''
