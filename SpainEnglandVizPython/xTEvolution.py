import mplsoccer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import arrowhead_marker

sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

data = pd.read_csv("EurosFinal2024-Spain v England.csv")
df = data.loc[:, ['expandedMinute', 'second', 'type',
                'outcomeType', 'shortName', 'xT',
                'x', 'y', 'endX', 'endY', 'teamName']]

df.dropna(inplace=True)

xT_spain = 0
xT_england = 0
stopMinute = 1
var_xTS = []
var_xTE = []
evo_min = []

for i, row in df.iterrows():
    if row['teamName'] == 'Spain':
        xT_spain += row['xT']
    else :
        xT_england += row['xT']
    if row['expandedMinute'] > stopMinute:
        var_xTS.append(xT_spain)
        var_xTE.append(xT_england)
        xT_spain = 0
        xT_england = 0
        stopMinute = row['expandedMinute'] + 1
        evo_min.append(row['expandedMinute'])


fig = plt.figure(figsize = (15, 10))

plt.plot(evo_min, var_xTS, linestyle='-', c='r', label='Spain')
plt.plot(evo_min, var_xTE, linestyle='-', c='c', label='England')

ax = fig.gca()
ax.set_xticks(np.arange(0, 96, 3), minor=True)
ax.set_xticks(np.arange(0, 96, 3))
ax.set_yticks(np.arange(-0.2,0.4, 0.05))
ax.set_yticks(np.arange(-0.2,0.4, 0.05), minor=True)
plt.grid()

plt.xlabel('Minutes')
plt.ylabel('xT')

plt.title('Expected threat (xT) cumulated per minute', fontsize = 20, fontweight = 'bold')
plt.legend(loc='best')

plt.xlim(0, 96)
plt.ylim(-0.2, 0.4)
plt.show()







