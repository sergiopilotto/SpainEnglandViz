import pandas as pd
import mplsoccer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("EurosFinal2024-Spain v England.csv")


# dataframe with successful passes

df_passes = dataframe.groupby('type')
df_passes = df_passes.get_group('Pass')
df_passes = df_passes.groupby('outcomeType')
df_passes = df_passes.get_group('Successful')



df_passes = df_passes.groupby('teamName')
df_passes_spain = df_passes.get_group('Spain')
df_passes_spainFH = df_passes_spain.groupby('period').get_group('FirstHalf')
df_passes_spainSH = df_passes_spain.groupby('period').get_group('SecondHalf')
df_passes_england = df_passes.get_group('England')
df_passes_england = df_passes_england.groupby('period')
df_passes_englandFH = df_passes_england.get_group('FirstHalf').loc[:,['x', 'y', 'endX', 'endY', 'outcomeType']]
df_passes_englandSH = df_passes_england.get_group('SecondHalf').loc[:,['x', 'y', 'endX', 'endY', 'outcomeType']]



sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

# Plot Spain first and second half

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor('black')


pitch.arrows(df_passes_spainFH.x, df_passes_spainFH.y,
             df_passes_spainFH.endX, df_passes_spainFH.endY, width = 2,
             headwidth=10, headlength=10, color=sc, ax=ax, label="Spain's successful passes")


ax_title = ax.set_title("Spain successful passes during the first half", color='white', fontsize=30, fontweight='bold')

plt.show()

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor('black')

pitch.arrows(df_passes_spainSH.x, df_passes_spainSH.y,
             df_passes_spainSH.endX, df_passes_spainSH.endY, width = 2,
             headwidth=10, headlength=10, color=sc, ax=ax, label="Spain's successful passes")


ax_title = ax.set_title("Spain successful passes during the second half", color='white', fontsize=30, fontweight='bold')
plt.show()

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor('black')

pitch.arrows(df_passes_englandFH.x, df_passes_englandFH.y,
             df_passes_englandFH.endX, df_passes_englandFH.endY, width = 2,
             headwidth=10, headlength=10, color=ec, ax=ax)


ax_title = ax.set_title("England successful passes during the first half", color='white', fontsize=30, fontweight='bold')

plt.show()

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor('black')

pitch.arrows(df_passes_englandSH.x, df_passes_englandSH.y,
             df_passes_englandSH.endX, df_passes_englandSH.endY, width = 2,
             headwidth=10, headlength=10, color=ec, ax=ax)


ax_title = ax.set_title("England successful passes during the second half", color='white', fontsize=30, fontweight='bold')


plt.show()



