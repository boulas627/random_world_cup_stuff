import pandas as pd
import numpy as np
import sys

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



print(countries_defeated)


# confederation breakdown of countries defeated 

confeds = ["Concacaf", "Comnebol", "Uefa", "CAF", "Asian Confederation", "Oceania"]

