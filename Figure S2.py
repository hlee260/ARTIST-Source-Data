'''Figure S2'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

datafile = pd.read_excel('Figure S2.xlsx')
time = datafile['Time']
data = datafile.loc[:, '0nM_raw':'100nM_normalized']
time = time - time[0]

# Plotting the avg data
lw = 2
plt.figure()
plt.plot(time, data['0nM_raw'], color=[1,0,0], linewidth=lw)
# Customize graph

fs = 20

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(0, 14000)
plt.xlim(0,270)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,4))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('RFU',fontsize=fs)

plt.savefig('FigureS2_0nM_raw.svg')


'''Below is for normalized results'''

plt.figure()
plt.plot(time, data['0nM_normalized'], color=[1,0,0], linewidth=lw)

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(0, 14000)
plt.xlim(0,270)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,4))
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('RFU',fontsize=fs)

plt.savefig('FigureS2_0nM_normalized.svg')

'''Code is also used for the 100 nM plot'''