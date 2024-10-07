import pandas as pd
import mplsoccer
from highlight_text import fig_text
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


dataframe = pd.read_csv("EurosFinal2024-Spain v England.csv")

"""
0) Number of passes
1) Passes precision
3) Number of tackles
2) Tackle precision
3) Possession
4) Interceptions
6) TakeOn
-) TakeOn precision
7) Fouls
8) Aerials won
9) Corners
"""

# Number of passes
spain_passes = dataframe.loc[(dataframe.type == 'Pass')
                             & (dataframe.teamName == 'Spain')].shape[0]
england_passes = dataframe.loc[(dataframe.type == 'Pass')
                               & (dataframe.teamName == 'England')].shape[0]

# Passes precision
spain_SuccPasses = dataframe.loc[(dataframe.type == 'Pass') &
                                 (dataframe.teamName == 'Spain') &
                                 (dataframe.outcomeType== 'Successful')].shape[0] / spain_passes
england_SuccPasses = dataframe.loc[(dataframe.type == 'Pass')
                                   & (dataframe.teamName == 'England')
                                   & (dataframe.outcomeType== 'Successful')].shape[0] / england_passes

# Number of tackles
spain_tackles = dataframe.loc[(dataframe.type == 'Tackle')
                              & (dataframe.teamName == 'Spain')].shape[0]
england_tackle = dataframe.loc[(dataframe.type == 'Tackle')
                               & (dataframe.teamName == 'England')].shape[0]

# Tackle Precision
spain_SuccTackles = dataframe.loc[(dataframe.type == 'Tackle')
                              & (dataframe.teamName == 'Spain')
                              & (dataframe.outcomeType == 'Successful')].shape[0] / spain_tackles
england_SuccTackles = dataframe.loc[(dataframe.type == 'Tackle')
                               & (dataframe.teamName == 'England')
                               & (dataframe.outcomeType == 'Successful')].shape[0] / england_tackle

# Possession
spain_poss = 0.63 # https://www.uefa.com/uefaeuro/match/2036211--spain-vs-england/statistics/
england_poss = 0.37 # https://www.uefa.com/uefaeuro/match/2036211--spain-vs-england/statistics/

# Balls recovered
spain_ballrecoveries = dataframe.loc[(dataframe.type == 'BallRecovery')
                                    & (dataframe.teamName == 'Spain')].shape[0]
england_ballrecoveries = dataframe.loc[(dataframe.type == 'BallRecovery')
                                      & (dataframe.teamName == 'England')].shape[0]

# Number of take on
spain_takeon = dataframe.loc[(dataframe.type == 'TakeOn')
                                 & (dataframe.teamName == 'Spain')].shape[0]
england_takeon = dataframe.loc[(dataframe.type == 'TakeOn')
                                   & (dataframe.teamName == 'England')].shape[0]

# TakeOn precision
spain_SuccTakeon = dataframe.loc[(dataframe.type == 'TakeOn') &
                                 (dataframe.teamName == 'Spain')
                                 & (dataframe.outcomeType == 'Successful')].shape[0] / spain_takeon
england_SuccTakeon = dataframe.loc[(dataframe.type == 'TakeOn')
                                   & (dataframe.teamName == 'England')
                                   & (dataframe.outcomeType == 'Successful')].shape[0] / england_takeon

# Fouls
spain_fouls = dataframe.loc[(dataframe.type == 'Foul')
                            & (dataframe.teamName == 'Spain')].shape[0]
england_fouls = dataframe.loc[(dataframe.type == 'Foul')
                              & (dataframe.teamName == 'England')].shape[0]

# Cards
spain_cards = dataframe.loc[(dataframe.type == 'Card')
                            & (dataframe.teamName == 'Spain')].shape[0]
england_cards = dataframe.loc[(dataframe.type == 'Card')
                              & (dataframe.teamName == 'England')].shape[0]

# Aerials won
spain_aerials = dataframe.loc[(dataframe.type == 'Aerial')
                              & (dataframe.teamName == 'Spain')
                              & (dataframe.outcomeType == 'Successful')].shape[0]
england_aerials = dataframe.loc[(dataframe.type == 'Aerial')
                                & (dataframe.teamName == 'England')
                                & (dataframe.outcomeType == 'Successful')].shape[0]

# Corners
spain_corners = dataframe.loc[(dataframe.type == 'CornerAwarded')
                              & (dataframe.teamName == 'Spain')
                              & (dataframe.outcomeType == 'Successful')].shape[0]
england_corners = dataframe.loc[(dataframe.type == 'CornerAwarded')
                                & (dataframe.teamName == 'England')
                                & (dataframe.outcomeType == 'Successful')].shape[0]


#### PIZZA PLOT

sc = "#9c1f1f" # spain color
ec = "#1eadba" # england color

params = [
    "Number of Passes",
    "Passes precision (%)",
    "Number of Tackles",
    "Tackle precision (%)",
    "Take On(s)",
    "Take On(s) precision (%)",
    "BallRecoveries",
    "Aerials won",
    "Corners",
    "Cards",
    "Possession"
]

spain_values = [
    spain_passes,
    round(spain_SuccPasses, 2),
    spain_tackles,
    round(spain_SuccTackles, 2),
    spain_takeon,
    round(spain_SuccTakeon, 2),
    spain_ballrecoveries,
    spain_aerials,
    spain_corners,
    spain_cards,
    spain_poss
]

england_values = [
    england_passes,
    round(england_SuccPasses, 2),
    england_tackle,
    round(england_SuccTackles, 2),
    england_takeon,
    round(england_SuccTakeon, 2),
    england_ballrecoveries,
    england_aerials,
    england_corners,
    england_cards,
    england_poss
]

min_range = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

max_range = [
    max(england_passes, spain_passes) + 100,
    1,
    max(spain_tackles, england_tackle) + 10,
    1,
    max(spain_takeon, england_takeon) + 2,
    0.4,
    max(spain_ballrecoveries, england_ballrecoveries) + 10,
    max(spain_aerials, england_aerials) + 2,
    max(spain_corners, england_corners) + 3,
    max(spain_cards, england_cards) + 1,
    0.80
]

baker = mplsoccer.PyPizza(
    params = params,
    min_range = min_range,
    max_range = max_range,
    background_color = 'black',
    straight_line_color = 'white',
    straight_line_lw = 1,
    last_circle_color = 'white',
    last_circle_lw = 2.5,
    other_circle_color = 'black',
    other_circle_lw = 0,
)

fig, ax = baker.make_pizza(
    spain_values,
    compare_values=england_values,
    figsize=(11,11),
    blank_alpha=0.4,
    param_location=105,
    kwargs_slices=dict(
        facecolor=sc, edgecolor="#000000",
        zorder=1, linewidth=1
    ),  # values to be used when plotting slices
    kwargs_compare=dict(
        facecolor=ec, edgecolor="black", zorder=3, linewidth=1,
    ),  # values to be used when plotting comparison slices
    kwargs_params=dict(
        color="white", fontsize=12, zorder=5,
        va="center"
    ),  # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor=sc,
            boxstyle="round,pad=0.2", lw=1,
        )
    ),  # values to be used when adding parameter-values
    kwargs_compare_values=dict(
        color="#000000", fontsize=12,
        zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor=ec,
            boxstyle="round,pad=0.2", lw=1
        )
    )
)

params_offset = [False, False, False, True, False, True, False, True, False, False, False]

baker.adjust_texts(params_offset, offset=-0.17, adj_comp_values=True)

fig_text(
    0.515, 0.99, "<Spain> vs <England>",
    size=17, fig=fig,
    highlight_textprops=[{"color": sc}, {"color": ec}],
    ha="center", color="white"
)

fig.text(
0.515, 0.935,
    "Euros Finals 2024",
    size=15,
    ha="center",
    color="white",
    fontstyle="italic",
)

plt.show()
