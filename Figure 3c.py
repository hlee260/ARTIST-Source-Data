import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# Import dataset
df = pd.read_excel('Figure 3c.xlsx')
df = df.set_index('Proteins')
fs = 17

ax = plt.axes()
plt.ylabel('Proteins [100 nM]', fontsize=fs-1)
plt.xticks(fontsize=fs)
plt.xlabel('dART', fontsize=fs)
ax.xaxis.tick_top()
plt.yticks(fontsize=fs - 3)


# plot a heatmap with annotation
sns.heatmap(df, annot=True, annot_kws={"size": fs-4}, cmap="Blues_r", cbar_kws={'label':'[Reacted Reporter]'})
ax.set_title('dART [10 nM]', size=fs - 1)
plt.xticks(fontsize=fs-3)
plt.yticks(fontsize=fs - 3)

cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=fs-3)

fig = plt.gcf()

fig.savefig('Figure 3c.svg')