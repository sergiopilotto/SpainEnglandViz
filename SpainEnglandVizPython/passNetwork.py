import pandas as pd
import mplsoccer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("EurosFinal2024-Spain v England.csv")
df_passes = dataframe.groupby('type').get_group('Pass')
df_passes = df_passes.groupby('outcomeType').get_group('Successful')
df_passes.relatedPlayerId = df_passes.relatedPlayerId.fillna('')


# renaming relatedPlayerId to receiverName


df_passes = df_passes.rename(columns={'relatedPlayerId': 'receiverName'})


for i in range(0, 1367):
    j = dataframe.iloc[i+1, 0]
    df_passes.loc[i, 'receiverName'] = dataframe.loc[j, 'shortName']



#### SPAIN FIRST HALF

df_passnet_spainFH = df_passes.loc[(df_passes.teamName=='Spain') & (df_passes.period=='FirstHalf'),['Unnamed: 0', 'shortName', 'receiverName', 'x', 'y' ,'endX', 'endY', 'expandedMinute']]

df_passnet_spainFH = df_passnet_spainFH.drop(717) # we drop the row that gives an error i.e. the last pass from the first period

# we select the 11 players that played the most

df_players11 = df_passnet_spainFH.groupby('shortName').agg({'expandedMinute': ['min', 'max']}).reset_index()
df_players11['totalMin'] = 0

for i in range(len(df_players11)):
    df_players11.iloc[i,-1] = df_players11.iloc[i,2] - df_players11.iloc[i,1]

df_players11 = df_players11.sort_values('totalMin', ascending=False).reset_index()
players11 = df_players11[0:11].shortName

df_passnet_spainFH = df_passnet_spainFH.loc[df_passnet_spainFH.shortName.isin(players11),:]
df_passnet_spainFH = df_passnet_spainFH.loc[df_passnet_spainFH.receiverName.isin(players11),:]

def nameTo3(name):
    name = name.replace(' ', '')
    name = name.replace('.', '')

    return (name[0]+name[1]+name[2]).upper()

df_passnet_spainFH.shortName = df_passnet_spainFH.shortName.map(nameTo3)
df_passnet_spainFH.receiverName = df_passnet_spainFH.receiverName.map(nameTo3)



df_scatter = pd.DataFrame()

# calculation of avg positions and circle size for each player

for i, name in enumerate(df_passnet_spainFH['shortName'].unique()):
    passx = df_passnet_spainFH.loc[df_passnet_spainFH['shortName']==name,'x'].to_numpy()
    recx = df_passnet_spainFH.loc[df_passnet_spainFH['shortName']==name,'endX'].to_numpy()
    passy = df_passnet_spainFH.loc[df_passnet_spainFH['shortName']==name,'y'].to_numpy()
    recy = df_passnet_spainFH.loc[df_passnet_spainFH['shortName']==name,'endY'].to_numpy()

    df_scatter.loc[i, 'shortName'] = name
    df_scatter.loc[i, 'x'] = np.mean(np.concatenate((passx, recx)))
    df_scatter.loc[i, 'y'] = np.mean(np.concatenate((passy, recy)))
    df_scatter.loc[i, 'numPasses'] = df_passnet_spainFH.loc[df_passnet_spainFH['shortName']==name].count().iloc[0]

df_scatter['marker_size'] = (df_scatter.numPasses / df_scatter.numPasses.max() * 2500)



# calculate the edges width

df_passnet_spainFH['pairKey'] = df_passnet_spainFH.apply(lambda x: "_".join(sorted([x["shortName"], x["receiverName"]])), axis=1)

df_lines = df_passnet_spainFH.groupby("pairKey").x.count().reset_index()
df_lines.rename({'x':'pass_count'}, axis='columns', inplace=True)

### CENTRALISATION
#https://soccermatics.readthedocs.io/en/latest/gallery/lesson1/plot_PassNetworks.html

df_numPasses = df_passnet_spainFH.groupby('shortName').x.count().reset_index()
df_numPasses.rename({'x':'passCount'}, axis='columns', inplace=True)
max_num = df_numPasses.passCount.max()
denom = 10*df_numPasses.passCount.max()
nom = (max_num - df_numPasses.passCount).sum()
centralisation_index = nom/denom
centralisation = "Index of centralisation: " + str(centralisation_index)

# plot

sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor("black")

pitch.scatter(df_scatter.x, df_scatter.y, s=df_scatter.marker_size, color=sc, edgecolors='black', ax=ax, zorder = 3)


for i,row in df_scatter.iterrows():
    pitch.annotate(row.shortName, xy=(row.x, row.y), c='white', ha='center', va='center', ax=ax, zorder=4)

df_scatter = df_scatter.reset_index()

for i, row in df_lines.iterrows():
    player = row.pairKey.split('_')[0]
    receiver = row.pairKey.split('_')[1]
    playerX = df_scatter.loc[df_scatter['shortName'] == player, 'x'].iloc[0]
    playerY = df_scatter.loc[df_scatter['shortName'] == player, 'y'].iloc[0]
    receiverX = df_scatter.loc[df_scatter['shortName'] == receiver, 'x'].iloc[0]
    receiverY = df_scatter.loc[df_scatter['shortName'] == receiver, 'y'].iloc[0]

    num_passes = row["pass_count"]

    line_width = (num_passes / df_lines['pass_count'].max() * 10)

    pitch.lines(playerX, playerY, receiverX, receiverY, alpha=1, lw=line_width, zorder=2, color="grey", ax = ax)

ax_title = ax.set_title("Spain passing network during the first half", fontsize = 30, color='white', fontweight='bold', ha='center')
fig.text(
0.515, 0.1,
    centralisation,
    size=15,
    ha="center",
    color="white",
    fontstyle="italic",
)


#plt.show()




### SPAIN SECOND HALF

df_passnet_spainSH = df_passes.loc[(df_passes.teamName=='Spain') & (df_passes.period=='SecondHalf'),['Unnamed: 0', 'shortName', 'receiverName', 'x', 'y' ,'endX', 'endY', 'expandedMinute']]

# we select the 11 players that played the most

df_players11 = df_passnet_spainSH.groupby('shortName').agg({'expandedMinute': ['min', 'max']}).reset_index()
df_players11['totalMin'] = 0

for i in range(len(df_players11)):
    df_players11.iloc[i,-1] = df_players11.iloc[i,2] - df_players11.iloc[i,1]

df_players11 = df_players11.sort_values('totalMin', ascending=False).reset_index()
players11 = df_players11[0:11].shortName

df_passnet_spainSH = df_passnet_spainSH.loc[df_passnet_spainSH.shortName.isin(players11),:]
df_passnet_spainSH = df_passnet_spainSH.loc[df_passnet_spainSH.receiverName.isin(players11),:]


df_passnet_spainSH.shortName = df_passnet_spainSH.shortName.map(nameTo3)
df_passnet_spainSH.receiverName = df_passnet_spainSH.receiverName.map(nameTo3)

df_scatter = pd.DataFrame()

# calculation of avg positions and circle size for each player

for i, name in enumerate(df_passnet_spainSH['shortName'].unique()):
    passx = df_passnet_spainSH.loc[df_passnet_spainSH['shortName']==name,'x'].to_numpy()
    recx = df_passnet_spainSH.loc[df_passnet_spainSH['shortName']==name,'endX'].to_numpy()
    passy = df_passnet_spainSH.loc[df_passnet_spainSH['shortName']==name,'y'].to_numpy()
    recy = df_passnet_spainSH.loc[df_passnet_spainSH['shortName']==name,'endY'].to_numpy()

    df_scatter.loc[i, 'shortName'] = name
    df_scatter.loc[i, 'x'] = np.mean(np.concatenate((passx, recx)))
    df_scatter.loc[i, 'y'] = np.mean(np.concatenate((passy, recy)))
    df_scatter.loc[i, 'numPasses'] = df_passnet_spainSH.loc[df_passnet_spainSH['shortName']==name].count().iloc[0]

df_scatter['marker_size'] = (df_scatter.numPasses / df_scatter.numPasses.max() * 2500)



# calculate the edges width

df_passnet_spainSH['pairKey'] = df_passnet_spainSH.apply(lambda x: "_".join(sorted([x["shortName"], x["receiverName"]])), axis=1)

df_lines = df_passnet_spainSH.groupby("pairKey").x.count().reset_index()
df_lines.rename({'x':'pass_count'}, axis='columns', inplace=True)

# centralisation
df_numPasses = df_passnet_spainSH.groupby('shortName').x.count().reset_index()
df_numPasses.rename({'x':'passCount'}, axis='columns', inplace=True)
max_num = df_numPasses.passCount.max()
denom = 10*df_numPasses.passCount.sum()
nom = (max_num - df_numPasses.passCount).sum()
centralisation_index = nom/denom
centralisation = "Index of centralisation: " + str(centralisation_index)



# plot

sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor("black")

pitch.scatter(df_scatter.x, df_scatter.y, s=df_scatter.marker_size, color=sc, edgecolors='black', ax=ax, zorder = 3)


for i,row in df_scatter.iterrows():
    pitch.annotate(row.shortName, xy=(row.x, row.y), c='white', ha='center', va='center', ax=ax, zorder=4)

df_scatter = df_scatter.reset_index()

for i, row in df_lines.iterrows():
    player = row.pairKey.split('_')[0]
    receiver = row.pairKey.split('_')[1]
    playerX = df_scatter.loc[df_scatter['shortName'] == player, 'x'].iloc[0]
    playerY = df_scatter.loc[df_scatter['shortName'] == player, 'y'].iloc[0]
    receiverX = df_scatter.loc[df_scatter['shortName'] == receiver, 'x'].iloc[0]
    receiverY = df_scatter.loc[df_scatter['shortName'] == receiver, 'y'].iloc[0]

    num_passes = row["pass_count"]

    line_width = (num_passes / df_lines['pass_count'].max() * 10)

    pitch.lines(playerX, playerY, receiverX, receiverY, alpha=1, lw=line_width, zorder=2, color="grey", ax = ax)

ax_title = ax.set_title("Spain passing network during the second half", fontsize = 30, color='white', fontweight='bold')

fig.text(0.5, 0.1, centralisation, fontstyle='italic', color='white', size=15, ha='center')

#plt.show()


#### ENGLAND FIRST HALF

df_passnet_englandFH = df_passes.loc[(df_passes.teamName=='England') & (df_passes.period=='FirstHalf'),['Unnamed: 0', 'shortName', 'receiverName', 'x', 'y' ,'endX', 'endY', 'expandedMinute']]

# we select the 11 players that played the most

df_players11 = df_passnet_englandFH.groupby('shortName').agg({'expandedMinute': ['min', 'max']}).reset_index()
df_players11['totalMin'] = 0

for i in range(len(df_players11)):
    df_players11.iloc[i,-1] = df_players11.iloc[i,2] - df_players11.iloc[i,1]

df_players11 = df_players11.sort_values('totalMin', ascending=False).reset_index()
players11 = df_players11[0:11].shortName

df_passnet_englandFH = df_passnet_englandFH.loc[df_passnet_englandFH.shortName.isin(players11),:]
df_passnet_englandFH = df_passnet_englandFH.loc[df_passnet_englandFH.receiverName.isin(players11),:]


df_passnet_englandFH.shortName = df_passnet_englandFH.shortName.map(nameTo3)
df_passnet_englandFH.receiverName = df_passnet_englandFH.receiverName.map(nameTo3)



df_scatter = pd.DataFrame()

# calculation of avg positions and circle size for each player

for i, name in enumerate(df_passnet_englandFH['shortName'].unique()):
    passx = df_passnet_englandFH.loc[df_passnet_englandFH['shortName']==name,'x'].to_numpy()
    recx = df_passnet_englandFH.loc[df_passnet_englandFH['shortName']==name,'endX'].to_numpy()
    passy = df_passnet_englandFH.loc[df_passnet_englandFH['shortName']==name,'y'].to_numpy()
    recy = df_passnet_englandFH.loc[df_passnet_englandFH['shortName']==name,'endY'].to_numpy()

    df_scatter.loc[i, 'shortName'] = name
    df_scatter.loc[i, 'x'] = np.mean(np.concatenate((passx, recx)))
    df_scatter.loc[i, 'y'] = np.mean(np.concatenate((passy, recy)))
    df_scatter.loc[i, 'numPasses'] = df_passnet_englandFH.loc[df_passnet_englandFH['shortName']==name].count().iloc[0]

df_scatter['marker_size'] = (df_scatter.numPasses / df_scatter.numPasses.max() * 2500)



# calculate the edges width

df_passnet_englandFH['pairKey'] = df_passnet_englandFH.apply(lambda x: "_".join(sorted([x["shortName"], x["receiverName"]])), axis=1)

df_lines = df_passnet_englandFH.groupby("pairKey").x.count().reset_index()
df_lines.rename({'x':'pass_count'}, axis='columns', inplace=True)


# centralisation
df_numPasses = df_passnet_englandFH.groupby('shortName').x.count().reset_index()
df_numPasses.rename({'x': 'passCount'}, inplace=True, axis='columns')
max_num = df_numPasses.passCount.max()
denom = df_numPasses.passCount.sum()*10
nom = (max_num - df_numPasses.passCount).sum()
centralisation_index = round(nom/denom, 4)
centralisation = "Index of centralisation: " + str(centralisation_index)


# plot

sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor("black")

pitch.scatter(df_scatter.x, df_scatter.y, s=df_scatter.marker_size, color=ec, edgecolors='black', ax=ax, zorder = 3)


for i,row in df_scatter.iterrows():
    pitch.annotate(row.shortName, xy=(row.x, row.y), c='white', ha='center', va='center', ax=ax, zorder=4)

df_scatter = df_scatter.reset_index()

for i, row in df_lines.iterrows():
    player = row.pairKey.split('_')[0]
    receiver = row.pairKey.split('_')[1]
    playerX = df_scatter.loc[df_scatter['shortName'] == player, 'x'].iloc[0]
    playerY = df_scatter.loc[df_scatter['shortName'] == player, 'y'].iloc[0]
    receiverX = df_scatter.loc[df_scatter['shortName'] == receiver, 'x'].iloc[0]
    receiverY = df_scatter.loc[df_scatter['shortName'] == receiver, 'y'].iloc[0]

    num_passes = row["pass_count"]

    line_width = (num_passes / df_lines['pass_count'].max() * 10)

    pitch.lines(playerX, playerY, receiverX, receiverY, alpha=1, lw=line_width, zorder=2, color="grey", ax = ax)

ax_title = ax.set_title("England passing network during the first half", color='white', fontsize=30, fontweight='bold')
fig.text(0.5, 0.1, centralisation, fontstyle='italic', color='white', size=15, ha='center')
#plt.show()



#### ENGLAND SECOND HALF

df_passnet_englandSH = df_passes.loc[(df_passes.teamName=='England') & (df_passes.period=='SecondHalf'),['Unnamed: 0', 'shortName', 'receiverName', 'x', 'y' ,'endX', 'endY', 'expandedMinute']]

# we select the 11 players that played the most

df_players11 = df_passnet_englandSH.groupby('shortName').agg({'expandedMinute': ['min', 'max']}).reset_index()
df_players11['totalMin'] = 0

for i in range(len(df_players11)):
    df_players11.iloc[i,-1] = df_players11.iloc[i,2] - df_players11.iloc[i,1]

df_players11 = df_players11.sort_values('totalMin', ascending=False).reset_index()
players11 = df_players11[0:11].shortName

df_passnet_englandSH = df_passnet_englandSH.loc[df_passnet_englandSH.shortName.isin(players11),:]
df_passnet_englandSH = df_passnet_englandSH.loc[df_passnet_englandSH.receiverName.isin(players11),:]



df_passnet_englandSH.shortName = df_passnet_englandSH.shortName.map(nameTo3)
df_passnet_englandSH.receiverName = df_passnet_englandSH.receiverName.map(nameTo3)



df_scatter = pd.DataFrame()

# calculation of avg positions and circle size for each player

for i, name in enumerate(df_passnet_englandSH['shortName'].unique()):
    passx = df_passnet_englandSH.loc[df_passnet_englandSH['shortName']==name,'x'].to_numpy()
    recx = df_passnet_englandSH.loc[df_passnet_englandSH['shortName']==name,'endX'].to_numpy()
    passy = df_passnet_englandSH.loc[df_passnet_englandSH['shortName']==name,'y'].to_numpy()
    recy = df_passnet_englandSH.loc[df_passnet_englandSH['shortName']==name,'endY'].to_numpy()

    df_scatter.loc[i, 'shortName'] = name
    df_scatter.loc[i, 'x'] = np.mean(np.concatenate((passx, recx)))
    df_scatter.loc[i, 'y'] = np.mean(np.concatenate((passy, recy)))
    df_scatter.loc[i, 'numPasses'] = df_passnet_englandSH.loc[df_passnet_englandSH['shortName']==name].count().iloc[0]

df_scatter['marker_size'] = (df_scatter.numPasses / df_scatter.numPasses.max() * 2500)



# calculate the edges width

df_passnet_englandSH['pairKey'] = df_passnet_englandSH.apply(lambda x: "_".join(sorted([x["shortName"], x["receiverName"]])), axis=1)

df_lines = df_passnet_englandSH.groupby("pairKey").x.count().reset_index()
df_lines.rename({'x':'pass_count'}, axis='columns', inplace=True)


# centralisation
df_numPasses = df_passnet_englandSH.groupby('shortName').x.count().reset_index()
df_numPasses.rename({'x': 'passCount'}, inplace=True, axis='columns')
max_num = df_numPasses.passCount.max()
denom = df_numPasses.passCount.sum()*10
nom = (max_num - df_numPasses.passCount).sum()
centralisation_index = round(nom/denom, 4)
centralisation = "Index of centralisation: " + str(centralisation_index)

# plot

sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

pitch = mplsoccer.Pitch(pitch_type='uefa', pitch_color='black', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor("black")

pitch.scatter(df_scatter.x, df_scatter.y, s=df_scatter.marker_size, color=ec, edgecolors='black', ax=ax, zorder = 3)


for i,row in df_scatter.iterrows():
    pitch.annotate(row.shortName, xy=(row.x, row.y), c='white', ha='center', va='center', ax=ax, zorder=4)

df_scatter = df_scatter.reset_index()

for i, row in df_lines.iterrows():
    player = row.pairKey.split('_')[0]
    receiver = row.pairKey.split('_')[1]
    playerX = df_scatter.loc[df_scatter['shortName'] == player, 'x'].iloc[0]
    playerY = df_scatter.loc[df_scatter['shortName'] == player, 'y'].iloc[0]
    receiverX = df_scatter.loc[df_scatter['shortName'] == receiver, 'x'].iloc[0]
    receiverY = df_scatter.loc[df_scatter['shortName'] == receiver, 'y'].iloc[0]

    num_passes = row["pass_count"]

    line_width = (num_passes / df_lines['pass_count'].max() * 10)

    pitch.lines(playerX, playerY, receiverX, receiverY, alpha=1, lw=line_width, zorder=2, color="grey", ax = ax)

ax_title = ax.set_title("England passing network during the second half", color='white', fontsize=30, fontweight='bold')
fig.text(0.5, 0.1, centralisation, color='white', size=15, fontstyle='italic', ha='center')
#plt.show()
