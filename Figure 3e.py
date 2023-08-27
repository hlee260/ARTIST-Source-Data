'''Rep1a'''

'''Data processing excel with python'''

import pandas as pd
import matplotlib.pyplot as plt

datafile = pd.read_excel('Figure3e.xlsx')
time = datafile['Time']
data = datafile.loc[:, 'O1_0 nM':'O3_1000 nM']
time = time - time[0]

# Plotting the data
lw = 3
plt.figure()
plt.plot(time, data['O1_0 nM'], color=[0,0,0.3], linewidth=lw)
plt.plot(time, data['O1_5 nM'], color=[0,0,0.5], linewidth=lw)
plt.plot(time, data['O1_10 nM'], color=[0,0,0.7], linewidth=lw)
plt.plot(time, data['O1_100 nM'], color=[0,0,1], linewidth=lw)
plt.plot(time, data['O1_1000 nM'], color=[0,0.2,1], linewidth=lw)
    
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
plt.ylabel('[Reacted O1 Reporter] (nM)',fontsize=fs)
# plt.legend(['0 nM IFN-γ', '5 nM IFN-γ','10 nM IFN-γ', '100 nM IFN-γ', '1000 nM IFN-γ'], loc='upper left', fontsize=11)
plt.savefig('Figure3e_O1.svg')