'''Data processing excel with python'''

import pandas as pd
import matplotlib.pyplot as plt

datafile = pd.read_excel('Figure3b_IFN.xlsx')
time = datafile['Time']
data = datafile.loc[:, '0 nM':'max_1000 nM']
time = time - time[0]

# Plotting results

lw = 2

plt.figure()

plt.plot(time, data['0 nM'], color=[0,0,0.2], alpha = 0.8, linewidth=lw)
plt.plot(time, data['5 nM'], color=[0,0,0.5], alpha = 0.8, linewidth=lw)
plt.plot(time, data['10 nM'], color=[0,0,0.8], alpha = 0.8, linewidth=lw)
plt.plot(time, data['100 nM'], color=[0,0,1],alpha = 0.8, linewidth=lw)
plt.plot(time, data['1000 nM'], color=[0,0.5,1], alpha = 0.8, linewidth=lw)
#Min and max plots
plt.plot(time, data['min_0 nM'], color=[0,0,0], linewidth=lw-1)
plt.plot(time, data['min_5 nM'], color=[0,0,0.5], linewidth=lw-1)
plt.plot(time, data['min_10 nM'], color=[0,0,0.8], linewidth=lw-1)
plt.plot(time, data['min_100 nM'], color=[0,0,1], linewidth=lw-1)
plt.plot(time, data['min_1000 nM'], color=[0,0.5,1], linewidth=lw-1)
plt.plot(time, data['max_0 nM'], color=[0,0,0], linewidth=lw-1)
plt.plot(time, data['max_5 nM'], color=[0,0,0.5], linewidth=lw-1)
plt.plot(time, data['max_10 nM'], color=[0,0,0.8], linewidth=lw-1)
plt.plot(time, data['max_100 nM'], color=[0,0,1], linewidth=lw-1)
plt.plot(time, data['max_1000 nM'], color=[0,0.5,1], linewidth=lw-1)

#Shades
plt.fill_between(time, data['min_0 nM'], data['max_0 nM'], color=[0,0,0.2], alpha=0.3, interpolate=True)
plt.fill_between(time, data['min_5 nM'], data['max_5 nM'], color=[0,0,0.5], alpha=0.2, interpolate=True)
plt.fill_between(time, data['min_10 nM'], data['max_10 nM'], color=[0,0,0.8], alpha=0.2, interpolate=True)
plt.fill_between(time, data['min_100 nM'], data['max_100 nM'], color=[0,0,1], alpha=0.1, interpolate=True)
plt.fill_between(time, data['min_1000 nM'], data['max_1000 nM'], color=[0,0.5,1], alpha=0.1, interpolate=True)


# Customize graph

fs = 20

plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.ylim(-10,110)
plt.xlim(0,240)
ax1 = plt.gca()
ax1.xaxis.set_tick_params(which='both',size=3,width=1,direction='in',top='on')
ax1.yaxis.set_tick_params(which='both',size=3,width=1,direction='in',right='on')
plt.xlabel('Time (min)',fontsize=fs)
plt.ylabel('[Reacted Reporter] (nM)',fontsize=fs)
plt.legend(['0 nM IFN', '5 nM IFN-γ', '10 nM IFN-γ', '100 nM IFN-γ', '1000 nM IFN-γ'], loc='upper left', fontsize=11)

plt.savefig('Figure 3b_IFN.svg')