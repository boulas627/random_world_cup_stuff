The purpose of this repository is mostly for me to mess around with some world cup data that I was able to capture from Kaggle. The link from Kaggle is https://www.kaggle.com/datasets/evangower/fifa-world-cup?resource=download&select=matches.csv. I enjoy building data visualizations by using the matplotlib python library. The following lines will provide a description of each Python file that I am running in this repository: 

goals_per_game.py
  This file reads data from "worldcups.csv" and this pulls world cup data from 1930 - 2018. This python script is meant to compare the goals per game in each world cup to see over time how the goals per game has changed. This is able to answer the question "How much of an attacking mindset are teams having in the world cup?". 
  
results_breakdown.py
  This file reads data from "matches.csv" and this includes match data for each world cup from 1930 - 2018. This python script allows users the chance to list any country in the world and in return the script will return a bar chart breaking down the users country results (wins, losses, draws) in their world cup history. If a country has never appeared in a world cup or the user misspells a country name, the results will have a zero in each column. 
