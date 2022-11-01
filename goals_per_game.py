import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt


csv_data = pd.read_csv("worldcups.csv")
df = pd.DataFrame(csv_data)

print(df["goals_scored"])

goals_per_game = []

for i in range(len(df)): 
	goal_fraction = (df.loc[i, "goals_scored"]) / (df.loc[i, "games"])
	goals_per_game.append(goal_fraction)


print(goals_per_game)

df["goals_per_game"] = goals_per_game

plt.plot(df["year"], df["goals_per_game"])
plt.title("Goals Per Game In Each World Cup")
plt.xlabel('World Cup Year')
plt.ylabel('Goals Per Game')
plt.show()