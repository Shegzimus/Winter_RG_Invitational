import pandas as pd
import numpy as np

df = pd.read_csv('RG_ WNTR Invitational - Sheet2.csv')

# Convert "50 GAMES" column to a boolean column

df['50 GAMES?'] = df['50 GAMES?'].map({'Y': True, 'N': False})

# print(df.info())

# Remove rows where POINTS is '-'

df = df.loc[df['POINTS']!= '-']

# Shuffle the dataframe to randomly assign players to teams
df = df.sample(frac=1, random_state=43).reset_index(drop=True)

df['POINTS'] = pd.to_numeric(df['POINTS'].replace(',', '', regex=True), errors='coerce')


# Group players by their main roles
grouped = df.groupby('MAIN ROLE')

# Find the minimum number of players in any role to determine how many full teams we can get
min_players = grouped.size().min()

# Create teams
teams = []
for i in range(min_players):
    team = []
    for role, players in grouped:
        team.append(players.iloc[i])  # Select one player from each role       
    teams.append(pd.DataFrame(team))
    

for i, team in enumerate(teams):
    total_POINTS = team['POINTS'].sum()
    avg_POINTS = team['POINTS'].mean()
    print(f"Team {i+1}:")
    print(team[['PLAYER POOL', 'MAIN ROLE', 'POINTS']])
    print(f"Average POINTS: {avg_POINTS}\n")
    print(f"Total POINTS: {total_POINTS}\n")
    print("\n")

















# # Declare team size
# team_size = 5

# # Calculate the number of teams of 5 given the general player count
# num_teams = len(df) // team_size

# # Split the dataframe into teams
# teams = [df.iloc[i:i+team_size] for i in range(0, len(df), team_size)]

# # Calculate average 'POINTS' value for each team
# for i, team in enumerate(teams):
#     avg_POINTS = team['POINTS'].mean()
#     print(f"Team {i+1}:")
#     print(team[['PLAYER POOL', 'POINTS']])
#     print(f"Average POINTS: {avg_POINTS}\n")