library(tidyverse)

# Read in the fish data:
fish <- read_csv("Fish.csv")

head(fish)
glimpse(fish)

# fish species available:
fish$Species |> unique() |> length()

# A linear model to predict the height of a given fish species based on the
# width:
