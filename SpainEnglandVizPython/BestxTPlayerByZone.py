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
df.xT = df.xT.apply(lambda x: round(x, 3))
spain_totalxT = df.groupby('teamName').get_group('England').xT.sum()

df = df.groupby('teamName').get_group("England")


pitch = mplsoccer.Pitch(pitch_type='uefa', positional=True, pitch_color='black', line_color='black', line_zorder=2)
fig, ax = pitch.draw(figsize=(15, 10))
fig.set_facecolor('black')

stats = pitch.bin_statistic_positional(df.x, df.y, df.xT, statistic='sum')
pitch.heatmap_positional(stats, ax=ax, cmap='coolwarm', edgecolors='black')
labels = pitch.label_heatmap(stats, color='black', fontsize=18,
                             ax=ax, ha='center', va='center', str_format='{:0.00}')

plt.title('England total xT per zone', fontweight='bold', c='white', fontsize=20)

plt.show()