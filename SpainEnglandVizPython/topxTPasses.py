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

df.sort_values('xT', ascending=False, inplace=True)
df_top10xT = df.head(10)
pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize = (15, 10))
fig.set_facecolor('black')

pitch.arrows(df_top10xT.groupby('teamName').get_group('Spain').x,
             df_top10xT.groupby('teamName').get_group('Spain').y,
             df_top10xT.groupby('teamName').get_group('Spain').endX,
             df_top10xT.groupby('teamName').get_group('Spain').endY,
             ax=ax, color='red', label = 'Spain', lw=1, edgecolor='black')
pitch.arrows(105-df_top10xT.groupby('teamName').get_group('England').x,
             df_top10xT.groupby('teamName').get_group('England').y,
             105-df_top10xT.groupby('teamName').get_group('England').endX,
             df_top10xT.groupby('teamName').get_group('England').endY,
             ax=ax, color='cyan', label = 'England', lw=1, edgecolor='black')



for i, row in df_top10xT.iterrows():
    if row['teamName'] == 'Spain':
        ax.annotate(row['shortName'] + ' ('+str(round(row['xT'], 3)) + ')',
                    (row['x'], row['y']+1), color='grey', weight='bold')
    else:
        ax.annotate(row['shortName'] + ' ('+str(round(row['xT'], 3)) + ')',
                    (105-row['x'], row['y']+1), color='grey', weight='bold')




legend = plt.legend(prop={'size': 15}, labelcolor='white', edgecolor='black', bbox_to_anchor=(0.9, 1.05), loc='upper left')
legend.get_frame().set_alpha(None)
legend.get_frame().set_facecolor((0, 0, 0, 0))
plt.title('The 10 passes with most xT', fontsize = 30, fontweight = 'bold', color = 'white')
plt.show()







