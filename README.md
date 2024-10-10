# Visualisation of the 2024 Euros Finals (Spains vs England)
I've used the dataset available [here](https://www.kaggle.com/datasets/rohanraoeravelli/euros-finals-dashboard) 
in order to create some visualisations to have a better understanding of what happened during the match. 


## Some general info
![Pizza](SpainEnglandVizPython/# Visualisation of the 2024 Euros Finals (Spains vs England)
I've used the dataset available [here](https://www.kaggle.com/datasets/rohanraoeravelli/euros-finals-dashboard) 
in order to create some visualisations to have a better understanding of what happened during the match. 


## Some general info
![Pizza](SpainEnglandVizPython/Plots/Pizza_SpainVsEngland.png)

Here we have some general information about the match. What really stands out are the amount of passes done by Spain, almost the double of England, and the difference in possession.\
Except the number of corners, the rest is not so different.

## Pass analysis
Since the main difference between both teams (according to the pizza plot) are the passes and the possession, I wanted to take a closer look.

### Histogram of passes by player
![PassesMatch](SpainEnglandVizPython/Plots/Hist_PassesByPlayer.png)
I wanted to know exactly how many passes each player did. 
The first six players with most passes are Spanish players: the 4 defenders, the left midfielder (Fabián Ruiz) and the left winger (Nico Williams). All of them have more than 40 passes.
England, in the other hand, only has 3 players with more than 40 passes: their goalkeeper (Pickford), one defender (Walker) and one midfielder (Rice).

### Pass plots
After knowing who were the players with the most passes, I thought it would be interesting to know where did thoses passes happen.\
I made a plot for each team and for each period for better readability.

![PassSpainFH](SpainEnglandVizPython/Plots/PassesSpainFH.png) 
![PassSpainSH](SpainEnglandVizPython/Plots/PassesSpainSH.png)
For the Spanish team, we see a big number of passes made in the opponent midfield, with somewhat of an arch going from the wingers positions back to the midfield specially during the first half.
In fact, we see a lot of pressure coming from the sides, reflecting on the importance of the wingers (Nico Williams on the leftside and Lamine Yamal on the rightside).\
During the second half, less passes seem to happen in the opponent midfield, but the arch is still there aswell as the pressure from the wingers.
![PassEnglandFH](SpainEnglandVizPython/Plots/PassesEnglandFH.png)
![PassEnglandSH](SpainEnglandVizPython/Plots/PassesEnglandSH.png)

For the English team, there is a clear difference between the two periods.\
During the first, few passes are made and the majority happens in their own field (midfield and defense).
But during the second period, they seem to play further and the arch appears aswell as the pressure from the wingers. They also seem to play more on the right side of the field.
This change in playstyle may be due to Spain scoring the first goal at the 47th minute.

### Passing networks
Let's see now the passing networks for both teams during both periods.\
I used an index of centralisation (i.e. how distributed the passes are between players), with 0 being totally decentralised and 1 being completely centralised in one player, in order to quantify a team's centralisation and compare it. Usually, the more centralised teams' passing networks are, the less succesfull the teams are. Here we have to keep in mind that the fewer the passes, the less accurate it is.\
More [here](https://soccermatics.readthedocs.io/en/latest/lesson1/passnetworksExample.html).

![PN_SpainFH](SpainEnglandVizPython/Plots/PN_SpainFH.png)

First, we see that the defense line is quite pushed, playing in the midfield, and then we see that Rodri is playing almost in the middle of the network, passing to everyone almost equally.\
Secondly we see several important sub-networks:
- There is one between Carvajal, Le Normand, Laporte and Cucurella, that allows to carry the ball from one side to another easily.
- There is also one between Laporte, Le Normand and Rodri, with Rodri being a key player since, after receiving the ball from Laporte and Le Normand, distributes the ball to everyone.
- We have the networks on the sides with Carvajal passing to Yamal and Cucurella distributing to Laporte, Ruiz and Williams.

Lastly, we see that the index of centralisation is quite high, but it does not seem to be a problem since it is really centralised on the defense and not on a single player that could be easily neutralised.


![PN_SpainSH](SpainEnglandVizPython/Plots/PN_SpainSH.png)

During the second half of the game, there are a few changes:
- The defense line goes back.
- The network is way more decentralised, with the lowest index of the match.
- Fabián Ruiz plays more in the middle, assuming part of Rodri's role during the first period.
- Carvajal plays way further, almost next to Yamal, in order to better distribute the ball (maybe also in order to cover Rodri's absence). He receives and gives more passes from/towards the midfield (Ruiz) that from/towards the defense (Le Normand).

![PN_EnglandFH](SpainEnglandVizPython/Plots/PN_EnglandFH.png)

First, we see that every player usually plays in their own field except for just two players: Bellingham and Saka. Foden should be playing further, closer to Saka and at the same level as Bellingham, since they are both wingers in this match.\
The various sub-networks here are:
- Stones, Walker and Pickford.
- Walker, Mainoo and Saka.
- Pickford, Stones, Rice and Guéhi.
- Jude Bellingham distributing to Shaw, Rice and Kane and Rice being the key player in the middle.

The index of centralisation is quite good (and better than the Spanish one for the first half) but we have to remember that the number of England passes is low for the first period.

![PN_EnglandSH](SpainEnglandVizPython/Plots/PN_EnglandSH.png)

We can see some changes here:
- More aggressive playstyle: they play further now.
- Foden is playing alongside Bellingham but with less passes.
- Rice is even more key to the distribution of the ball: strong edges to Stones, Guéhi, Bellingham and Walker.
- Walker and Guéhi have bigger roles in the sides: Guéhi passes to Stones, Rice, Bellingham and Shaw, Walker has a strong edge with Saka and distributes more the ball (like Carvajal).
- Index of centralisation is higher.


## Players heatmaps

After having a look at the passes of the teams, we are going to concentrate on the wingers of both teams using their heatmaps.

### Nico Williams' heatmap
![NW_heatmap](SpainEnglandVizPython/Plots/Heatmap_NicoWilliams.png)

### Lamine Yamal's heatmap
![LM_heatmap](SpainEnglandVizPython/Plots/Heatmap_LamineYamal.png)

### Jude Bellingham's heatmap
![JB_heatmap](SpainEnglandVizPython/Plots/Heatmap_JudeBellingham.png)

### Phil Foden's heatmap
![PH_heatmap](SpainEnglandVizPython/Plots/Heatmap_PhilFoden.png)

We see that the Spanish players are more aggressive than the English players. Lamine Yamal seems to never go in Spain's field, and Phil Foden has a really spreaded heatmap.

## Process mining for the last two actions leading to shots
### Spain process map for the last two actions leading to shots (relative-antecedent)
![PMap_Spain](SpainEnglandVizR/Plots/ProcessMap_SpainLast2Actions.png)
### Spain process matrix for the last two actions leading to shots (relative-antecedent)
![PMat_Spain](SpainEnglandVizR/Plots/ProcessMatrix_SpainLast2Actions.png)
### England process map for the last two actions leading to shots (relative-antecedent)
![PMap_England](SpainEnglandVizR/Plots/ProcessMap_EnglandLast2Actions.png)
### England process matrix for the last two actions leading to shots (relative-antecedent)
![PMat_England](SpainEnglandVizR/Plots/ProcessMatrix_EnglandLast2Actions.png)


## Expected Threat (xT) analysis
### Total xT by player
![Barplot_totalxT](SpainEnglandVizPython/Plots/Barplot_totalxT.png)
### Expected Threat cumulated by minute
![Evo_xTPerMin](SpainEnglandVizPython/Plots/ExpectedThreatPerMinute.png)
### The 10 passes with most xT
![Top10PassesxT](SpainEnglandVizPython/Plots/PassesMostxT.png)


## Ressources used
I essentially used the [mplsoccer documentation](https://mplsoccer.readthedocs.io/en/latest/#) and the [soccermathics website](https://soccermatics.readthedocs.io/en/latest/), 
with the latter particularly for the passing networks and their centralisation. 
This project was entirely made with Python and these librairies: pandas, matplotlib, numpy, mplsoccer, seaborn, highlight_text.\
The dataset is in csv format.Plots/Pizza_SpainVsEngland.png)

Here we have some general information about the match. What really stands out are the amount of passes done by Spain, almost the double of England, and the difference in possession.\
Except the number of corners, the rest is not so different.

## Pass analysis
Since the main difference between both teams (according to the pizza plot) are the passes and the possession, I wanted to take a closer look.

### Histogram of passes by player
![PassesMatch](SpainEnglandVizPython/Plots/Hist_PassesByPlayer.png)
I wanted to know exactly how many passes each player did. 
The first six players with most passes are Spanish players: the 4 defenders, the left midfielder (Fabián Ruiz) and the left winger (Nico Williams). All of them have more than 40 passes.
England, in the other hand, only has 3 players with more than 40 passes: their goalkeeper (Pickford), one defender (Walker) and one midfielder (Rice).

### Pass plots
After knowing who were the players with the most passes, I thought it would be interesting to know where did thoses passes happen.\
I made a plot for each team and for each period for better readability.

![PassSpainFH](SpainEnglandVizPython/Plots/PassesSpainFH.png) 
![PassSpainSH](SpainEnglandVizPython/Plots/PassesSpainSH.png)
For the Spanish team, we see a big number of passes made in the opponent midfield, with somewhat of an arch going from the wingers positions back to the midfield specially during the first half.
In fact, we see a lot of pressure coming from the sides, reflecting on the importance of the wingers (Nico Williams on the leftside and Lamine Yamal on the rightside).\
During the second half, less passes seem to happen in the opponent midfield, but the arch is still there aswell as the pressure from the wingers.
![PassEnglandFH](SpainEnglandVizPython/Plots/PassesEnglandFH.png)
![PassEnglandSH](SpainEnglandVizPython/Plots/PassesEnglandSH.png)

For the English team, there is a clear difference between the two periods.\
During the first, few passes are made and the majority happens in their own field (midfield and defense).
But during the second period, they seem to play further and the arch appears aswell as the pressure from the wingers. They also seem to play more on the right side of the field.
This change in playstyle may be due to Spain scoring the first goal at the 47th minute.

### Passing networks
Let's see now the passing networks for both teams during both periods.\
I used an index of centralisation (i.e. how distributed the passes are between players), with 0 being totally decentralised and 1 being completely centralised in one player, in order to quantify a team's centralisation and compare it. Usually, the more centralised teams' passing networks are, the less succesfull the teams are. Here we have to keep in mind that the fewer the passes, the less accurate it is.\
More [here](https://soccermatics.readthedocs.io/en/latest/lesson1/passnetworksExample.html).

![PN_SpainFH](SpainEnglandVizPython/Plots/PN_SpainFH.png)

First, we see that the defense line is quite pushed, playing in the midfield, and then we see that Rodri is playing almost in the middle of the network, passing to everyone almost equally.\
Secondly we see several important sub-networks:
- There is one between Carvajal, Le Normand, Laporte and Cucurella, that allows to carry the ball from one side to another easily.
- There is also one between Laporte, Le Normand and Rodri, with Rodri being a key player since, after receiving the ball from Laporte and Le Normand, distributes the ball to everyone.
- We have the networks on the sides with Carvajal passing to Yamal and Cucurella distributing to Laporte, Ruiz and Williams.

Lastly, we see that the index of centralisation is quite high, but it does not seem to be a problem since it is really centralised on the defense and not on a single player that could be easily neutralised.


![PN_SpainSH](SpainEnglandVizPython/Plots/PN_SpainSH.png)

During the second half of the game, there are a few changes:
- The defense line goes back.
- The network is way more decentralised, with the lowest index of the match.
- Fabián Ruiz plays more in the middle, assuming part of Rodri's role during the first period.
- Carvajal plays way further, almost next to Yamal, in order to better distribute the ball (maybe also in order to cover Rodri's absence). He receives and gives more passes from/towards the midfield (Ruiz) that from/towards the defense (Le Normand).

![PN_EnglandFH](SpainEnglandVizPython/Plots/PN_EnglandFH.png)

First, we see that every player usually plays in their own field except for just two players: Bellingham and Saka. Foden should be playing further, closer to Saka and at the same level as Bellingham, since they are both wingers in this match.\
The various sub-networks here are:
- Stones, Walker and Pickford.
- Walker, Mainoo and Saka.
- Pickford, Stones, Rice and Guéhi.
- Jude Bellingham distributing to Shaw, Rice and Kane and Rice being the key player in the middle.

The index of centralisation is quite good (and better than the Spanish one for the first half) but we have to remember that the number of England passes is low for the first period.

![PN_EnglandSH](SpainEnglandVizPython/Plots/PN_EnglandSH.png)

We can see some changes here:
- More aggressive playstyle: they play further now.
- Foden is playing alongside Bellingham but with less passes.
- Rice is even more key to the distribution of the ball: strong edges to Stones, Guéhi, Bellingham and Walker.
- Walker and Guéhi have bigger roles in the sides: Guéhi passes to Stones, Rice, Bellingham and Shaw, Walker has a strong edge with Saka and distributes more the ball (like Carvajal).
- Index of centralisation is higher.


## Players heatmaps

After having a look at the passes of the teams, we are going to concentrate on the wingers of both teams using their heatmaps.

### Nico Williams' heatmap
![NW_heatmap](SpainEnglandVizPython/Plots/Heatmap_NicoWilliams.png)

### Lamine Yamal's heatmap
![LM_heatmap](SpainEnglandVizPython/Plots/Heatmap_LamineYamal.png)

### Jude Bellingham's heatmap
![JB_heatmap](SpainEnglandVizPython/Plots/Heatmap_JudeBellingham.png)

### Phil Foden's heatmap
![PH_heatmap](SpainEnglandVizPython/Plots/Heatmap_PhilFoden.png)

We see that the Spanish players are more aggressives than the English players. Lamine Yamal seems to never go in Spain's field, and Phil Foden has a really spreaded heatmap.

## Process mining for the last two actions leading to shots
### Spain process map for the last two actions leading to shots (relative-antecedent)
![PMap_Spain](SpainEnglandVizR/Plots/ProcessMap_SpainLast2Actions.png)
### Spain process matrix for the last two actions leading to shots (relative-antecedent)
![PMat_Spain](SpainEnglandVizR/Plots/ProcessMatrix_SpainLast2Actions.png)
### England process map for the last two actions leading to shots (relative-antecedent)
![PMap_England](SpainEnglandVizR/Plots/ProcessMap_EnglandLast2Actions.png)
### England process matrix for the last two actions leading to shots (relative-antecedent)
![PMat_England](SpainEnglandVizR/Plots/ProcessMatrix_EnglandLast2Actions.png)

## Ressources used
I essentially used the [mplsoccer documentation](https://mplsoccer.readthedocs.io/en/latest/#) and the [soccermathics website](https://soccermatics.readthedocs.io/en/latest/), 
with the latter particularly for the passing networks and their centralisation. 
This project was entirely made with Python and these librairies: pandas, matplotlib, numpy, mplsoccer, seaborn, highlight_text.\
The dataset is in csv format.
