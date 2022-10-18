import pandas as pd
import numpy as np
import sys
import matplotlib as plt


def world_cup_victories_sum(country_name, world_cup_df):
	countries_defeated = 0 
	
	for i in range(len(world_cup_df["winning_team"])): 
		if world_cup_df["winning_team"][i] == country_name: 
			countries_defeated += 1

	return countries_defeated

def world_cup_losses_sum(country_name, world_cup_df):

	countries_lost_to = 0

	for i in range(len(world_cup_df["losing_team"])): 
		if world_cup_df["losing_team"][i] == country_name: 
			countries_lost_to += 1

	return countries_lost_to

def world_cup_draws_sum(country_name, world_cup_df): 
	countries_drawn = 0

	for i in range(len(world_cup_df["outcome"])): 
		if world_cup_df["outcome"][i] == "D": 

			if world_cup_df["home_team"][i] == country_name: 
				countries_drawn += 1

			if world_cup_df["away_team"][i] == country_name:
				countries_drawn += 1 

	return countries_drawn


df = pd.read_csv("matches.csv")

df = pd.DataFrame(df)


user_country = input("Please input your countries name: ")

wins = world_cup_victories_sum(user_country, df)
losses = world_cup_losses_sum(user_country, df)
draws = world_cup_draws_sum(user_country, df)

df_results = pd.DataFrame()


# x_axis = ['Wins', 'Draws', 'Losses']
# y_axis = [ 10, 10, 20 ]

df_results['Wins'] = wins
df_results['Draws'] = draws
df_results['Losses'] = losses

df_results = pd.DataFrame([wins, draws, losses], columns=["wins", "draws", "losses"])
print(df_results)

# x_axis = ['Wins', 'Draws', 'Losses']
# y_axis = [ wins, draws, losses ]

# graph = df_results.plot.bar()




