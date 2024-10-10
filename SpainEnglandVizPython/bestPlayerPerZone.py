from cProfile import label

import mplsoccer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr


df = pd.read_csv("EurosFinal2024-Spain v England.csv")
df = df.loc[:, ['expandedMinute', 'second', 'type',
                'outcomeType', 'shortName', 'xT',
                'x', 'y', 'endX', 'endY', 'teamName']]

df.dropna(inplace=True)

# creation of zones (xstart, ystart, xend, yend)
zones=[(0, 54, 16.5, 68),
(0, 13.8, 16.5, 54),
(0, 0, 16.5, 13.8),
(16.5, 54, 34.5, 68),
(34.5, 54, 52.5, 68),
(16.5, 43.2, 52.5, 54),
(16.5, 24.8, 52.5, 43.2),
(16.5, 13.8, 52.5, 24.8),
(16.5, 0, 34.5, 13.8),
(34.5, 0, 52.5, 13.8),
(52.5, 54, 70.5, 68),
(70.5, 54, 88.5, 68),
(52.5, 43.2, 88.5, 54),
(52.5, 24.8, 88.5, 43.2),
(52.5, 13.8, 88.5, 24.8),
(52.5, 0, 70.5, 13.8),
(70.5, 0, 88.5, 13.8),
(88.5, 54, 105, 68),
(88.5, 13.8, 105, 54),
(88.5, 0, 105, 13.8)]


# initialization of a dataset per zone
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()
df8 = pd.DataFrame()
df9 = pd.DataFrame()
df10 = pd.DataFrame()
df11 = pd.DataFrame()
df12 = pd.DataFrame()
df13 = pd.DataFrame()
df14 = pd.DataFrame()
df15 = pd.DataFrame()
df16 = pd.DataFrame()
df17 = pd.DataFrame()
df18 = pd.DataFrame()
df19 = pd.DataFrame()
df20 = pd.DataFrame()

list_dfZones = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11,
                df12, df13, df14, df15, df16, df17, df18, df19, df20]


for df_zone in list_dfZones:
    df_zone.insert(0, 'shortName', '')
    df_zone.insert(1, 'xT', 0)
    df_zone.insert(2, 'x', 0)
    df_zone.insert(3, 'y', 0)
    df_zone.insert(4, 'teamName', '')


# separate the initial dataframe into the 20 zone datasets

for i, row in df.iterrows():
    for j, zone in enumerate(zones):
        if zone[0] <= row.x <= zone[2] and zone[1] <= row.y <= zone[3]:
            list_dfZones[j].loc[i, 'shortName'] = row.shortName
            list_dfZones[j].loc[i, 'x'] = row.x
            list_dfZones[j].loc[i, 'y'] = row.y
            list_dfZones[j].loc[i, 'xT'] = row.xT


# creation of the last dataset with the best players and their zones

df_test = df12.groupby('shortName').xT.sum().sort_values(ascending=False)

df_bestPlayers = pd.DataFrame()
df_bestPlayers.insert(0, 'shortName', '')
df_bestPlayers.insert(1, 'xT', 0)
df_bestPlayers.insert(2, 'x', 0)
df_bestPlayers.insert(3, 'y', 0)
df_bestPlayers.insert(4, 'zone', '')

for i, df_zone in enumerate(list_dfZones):
    df_bestPlayers.loc[i, 'shortName'] = (
        df_zone.groupby('shortName').xT.sum().sort_values(ascending=False).index[0])
    df_bestPlayers.loc[i, 'xT'] = (
        df_zone.groupby('shortName').xT.sum().sort_values(ascending=False)[0]
    )
    # use a point from the zone
    df_bestPlayers.loc[i, 'x'] = (zones[i][0] + zones[i][2])*0.5
    df_bestPlayers.loc[i, 'y'] = (zones[i][1] + zones[i][3])*0.5
    df_bestPlayers.loc[i, 'zone'] = i+1

### PLOT
pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white',
                        line_zorder=0, positional=True, positional_color='white', positional_linestyle="--")
fig, ax = pitch.draw(figsize=(15, 10))
fig.set_facecolor('black')

players_spain = df.groupby('teamName').get_group('Spain').loc[:,'shortName'].dropna().unique()
players_england = df.groupby('teamName').get_group('England').loc[:,'shortName'].dropna().unique()


for i, row in df_bestPlayers.iterrows():
    player = row.shortName
    if player in players_spain:
        ax.text(row.x, row.y, player, color='red',
                ha='center', va='center', size=15,
                bbox=dict(boxstyle="round,pad=0.5", fc="black", ec="red", lw=2), label='Spain')

    else:
        ax.text(row.x, row.y, player, color='cyan',
                ha='center', va='center', size=15,
                bbox=dict(boxstyle="round,pad=0.5", fc="black", ec="cyan", lw=2), label='England')


### just for the legend
plt.scatter(x=-3, y=0, c='red', label='Spain', alpha=1)
plt.scatter(x=-3, y=0, c='cyan', label='England', alpha=1)
plt.scatter(x=-3, y=0, c='black', alpha=1, s =50)

legend = plt.legend(prop={'size': 15}, labelcolor='white', edgecolor='black', bbox_to_anchor=(1, 1.05), loc='upper right')
legend.get_frame().set_alpha(None)
legend.get_frame().set_facecolor((0, 0, 0, 0))
plt.title("Best player per zone based on their xT", color='white', fontweight='bold', fontsize=30)
plt.show()

