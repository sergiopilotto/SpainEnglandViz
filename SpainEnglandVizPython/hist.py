import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import fontManager

dataframe = pd.read_csv('EurosFinal2024-Spain v England.csv')
df_passes = dataframe.groupby('type').get_group('Pass')



fig = plt.figure(figsize=[34, 20])


sns.set_style(rc={'axes.edgecolor': 'black'})

sns.histplot(data=df_passes, x='shortName', hue='teamName', palette=["#1eadba", "#9c1f1f"])

plt.show()



