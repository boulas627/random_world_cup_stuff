import pandas as pd
import numpy as np
import sys
import matplotlib as plt


def world_cup_victories(country_name, world_cup_df):
	countries_defeated = [] 
	
	for i in range(len(world_cup_df["winning_team"])): 
		if world_cup_df["winning_team"][i] == country_name: 
			countries_defeated.append(world_cup_df["losing_team"][i])

	return countries_defeated

def world_cup_losses(country_name, world_cup_df):

	countries_lost_to = []

	for i in range(len(world_cup_df["losing_team"])): 
		if world_cup_df["losing_team"][i] == country_name: 
			countries_lost_to.append(world_cup_df["winning_team"][i])

	return countries_lost_to

df = pd.read_csv("matches.csv")

df = pd.DataFrame(df)

print(df.columns)

united_states_wins = 0

for team in df['winning_team']: 
	
	if team == "United States": 
		united_states_wins += 1

print(united_states_wins)

countries_defeated = []

for i in range(len(df["winning_team"])): 

	# print(df["losing_team"][i])
	if df["winning_team"][i] == "United States": 
		countries_defeated.append(df["losing_team"][i])
		# print(df["losing_team"][i])



print(world_cup_losses("Senegal", df))

sys.exit()


match_results = ["Win", "Loss", "Draw"]
 
for row in df.iterrows(): 
	print(row)
	# if row["home_team"] == "United States" or row["away_team"] == "United States": 
	# 	print("I")




