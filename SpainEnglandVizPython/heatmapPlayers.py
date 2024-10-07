import pandas as pd
import mplsoccer
from highlight_text import fig_text
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import cmasher as cmr

from plotPasses import ax_title

dataframe = pd.read_csv("EurosFinal2024-Spain v England.csv")


# dataframes with locations of players actions
df_yamal = dataframe.groupby('name').get_group('Lamine Yamal').loc[:, ['x', 'y']]
df_nico = dataframe.groupby('name').get_group('Nico Williams').loc[:, ['x', 'y']]
df_bellingham = dataframe.groupby('name').get_group('Jude Bellingham').loc[:, ['x','y']]
df_foden = dataframe.groupby('name').get_group('Phil Foden').loc[:, ['x','y']]


# LAMINE YAMAL

pitch = mplsoccer.VerticalPitch(line_color='white', line_zorder=2, pitch_color='black', pitch_type='uefa')
fig, ax = pitch.draw(figsize=(15, 18))
fig.set_facecolor('black')
kde = pitch.kdeplot(df_yamal.x, df_yamal.y,
                    ax=ax,
                    fill = True,
                    levels = 100,
                    thresh = 0,
                    cmap = cmr.ember
                    )

ax_title = ax.set_title("Lamine Yamal's heatmap", fontweight='bold', color='white', fontsize=30)



# NICO WILLIAMS


kde = pitch.kdeplot(df_nico.x, df_nico.y,
                    ax=ax,
                    fill = True,
                    levels = 100,
                    thresh = 0,
                    cmap = cmr.ember
                    )

ax_title = ax.set_title("Nico Williams' heatmap", fontweight='bold', color='white', fontsize=30)



# JUDE BELLINGHAM

kde = pitch.kdeplot(df_bellingham.x, df_bellingham.y,
                    ax=ax,
                    fill = True,
                    levels = 100,
                    thresh = 0,
                    cmap = cmr.freeze
                    )

ax_title = ax.set_title("Jude Bellingham's heatmap", fontweight='bold', color='white', fontsize=30)



# PHIL FODEN

kde = pitch.kdeplot(df_foden.x, df_foden.y,
                    ax=ax,
                    fill = True,
                    levels = 100,
                    thresh = 0,
                    cmap = cmr.freeze
                    )

ax_title = ax.set_title("Phil Foden's heatmap", fontweight='bold', color='white', fontsize=30)

plt.show()




