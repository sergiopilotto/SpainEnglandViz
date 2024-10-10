import mplsoccer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("EurosFinal2024-Spain v England.csv")

df_xT = df.loc[:, ['Unnamed: 0', 'xT', 'shortName', 'x', 'y', 'endX', 'endY', 'expandedMinute', 'second', 'teamName', 'type']]

df_xT.dropna(inplace=True)
df_xTSpain = df_xT.groupby('teamName').get_group('Spain')
df_xTEngland = df_xT.groupby('teamName').get_group('England')


df_xTSpainGT0 = df_xTSpain.loc[(df_xTSpain.xT > 0.02), :]

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(15, 10))
fig.set_facecolor('black')

pitch.arrows(df_xTSpainGT0.x, df_xTSpainGT0.y, df_xTSpainGT0.endX, df_xTSpainGT0.endY,
             ax=ax, color='red', linewidth=1, edgecolor='black')

for i, row in df_xTSpainGT0.iterrows():
    ax.annotate(row.shortName + ' ' + str(round(row.xT, 3)), (row.x, row.y),
                color='grey', fontweight='bold')

plt.title('Spain passes with an xT superior to .02', fontweight='bold', color='white', fontsize=20)

plt.show()

df_xTEnglandGT0 = df_xTEngland.loc[df_xTEngland.xT > 0.02, :]

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(15, 10))
fig.set_facecolor('black')

pitch.arrows(df_xTEnglandGT0.x, df_xTEnglandGT0.y, df_xTEnglandGT0.endX, df_xTEnglandGT0.endY,
             ax=ax, color='cyan', linewidth=1, edgecolor='black')

for i, row in df_xTEnglandGT0.iterrows():
    ax.annotate(row.shortName + ' ' + str(round(row.xT, 3)), (row.x, row.y),
                color='grey', fontweight='bold')

plt.title('England passes with an xT superior to .02', fontweight='bold', color='white', fontsize=20)

plt.show()