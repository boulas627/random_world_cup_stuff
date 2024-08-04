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

def world_cup_draws(country_name, world_cup_df): 
	countries_drawn = []

	for i in range(len(world_cup_df["outcome"])): 
		if world_cup_df["outcome"][i] == "D": 

			if world_cup_df["home_team"][i] == country_name: 
				countries_drawn.append(world_cup_df["away_team"][i])

			if world_cup_df["away_team"][i] == country_name:
				countries_drawn.append(world_cup_df["home_team"][i])

	return countries_drawn


df = pd.read_csv("matches.csv")

df = pd.DataFrame(df)

user_country = input("Please input your countries name: ")

print("World Cup Draws")
print(world_cup_draws(user_country, df))

print("World Cup Losses")
print(world_cup_losses(user_country, df))

print("World Cup Victories")
print(world_cup_victories(user_country, df))



# match_results = ["Win", "Loss", "Draw"]
 
# for row in df.iterrows(): 
# 	print(row)
	




