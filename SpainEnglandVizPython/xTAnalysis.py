import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("EurosFinal2024-Spain v England.csv")
df = data.loc[:, ['expandedMinute', 'second', 'type',
                'outcomeType', 'shortName', 'xT',
                'x', 'y', 'endX', 'endY', 'teamName']]



df_xTSpain = df.groupby('teamName').get_group('Spain')
df_xTSpain.dropna(inplace=True)

df_xTEngland = df.groupby('teamName').get_group('England')
df_xTEngland.dropna(inplace=True)

df_testS = df_xTSpain.sort_values(by='xT', ascending=True).reset_index()
df_testE = df_xTEngland.sort_values(by='xT', ascending=True).reset_index()

print(df_testS.xT.mean())
print(df_testE.xT.mean())

df_playersxT = pd.DataFrame()
df_playersxT.insert(0, "players", df.loc[:, 'shortName'].unique())
df_playersxT.dropna(inplace=True)

df_playersxT.insert(1, "xT_mean", 0)
df_playersxT.insert(2, "xT_total", 0)

for i, row in df_playersxT.iterrows():
    mean = df.groupby('shortName').get_group(row['players'])['xT'].mean()
    df_playersxT.at[i, 'xT_mean'] = mean
    total = df.groupby('shortName').get_group(row['players'])['xT'].sum()
    df_playersxT.at[i, 'xT_total'] = total

df_playersxT.dropna(inplace=True)
df_playersxT = df_playersxT.sort_values(by='xT_total', ascending=False).reset_index()
