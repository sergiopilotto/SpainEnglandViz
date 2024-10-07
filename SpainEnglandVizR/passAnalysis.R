setwd("~/Projets/SpainEnglandEuros")
data <- read.csv("EurosFinal2024-Spain v England.csv")

#creation of a dataset formed of passes
df_passes <- data[data$type=="Pass",]

#cleaning of df_passes


df_passes <- df_passes[,c("X", "eventId", "teamId", "teamName", "minute", 
                          "second", "x", "y", "endX", "endY", "type", "period", 
                          "outcomeType", "playerId", "shortName", "position")]

# creation of a dataset for each team

df_passes_spain <- df_passes[df_passes$teamId==338,]
df_passes_england <- df_passes[df_passes$teamId==345,]

# visualisation of passes
{
  success_passes_spain <- df_passes_spain[,"outcomeType"]
  i = 1
  for (var in success_passes_spain) {
    if (var == "Successful") {
      success_passes_spain[i] = 1
    } else {
      success_passes_spain[i] = 0
    }
    i = i+1
  }
  
  success_passes_spain <- as.numeric(success_passes_spain)
  
  hs <- hist(success_passes_spain, breaks = 2)
  print("Proportion of successful passes : ")
  hs$counts[2] / (hs$counts[2]+hs$counts[1])
  
}
{
  success_passes_england <- df_passes_england[,"outcomeType"]
  i = 1
  for (var in success_passes_england) {
    if (var == "Successful") {
      success_passes_england[i] = 1
    } else {
      success_passes_england[i] = 0
    }
    i = i+1
  }
  
  success_passes_england <- as.numeric(success_passes_england)
  
  he <- hist(success_passes_england, breaks = 2)
  
  print("Proportion of successful passes : ")
  he$counts[2] / (he$counts[2]+he$counts[1])
  
}





