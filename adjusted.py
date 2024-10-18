import pandas as pd
import numpy as np

df = pd.read_csv('RG_ WNTR Invitational - Sheet2.csv')

# Convert "50 GAMES" column to a boolean column

df['50 GAMES?'] = df['50 GAMES?'].map({'Y': True, 'N': False})

# print(df.info())

# Remove rows where ADJUSTED is '-'

df = df.loc[df['ADJUSTED']!= '-']

# Shuffle the dataframe to randomly assign players to teams
df = df.sample(frac=1, random_state=43).reset_index(drop=True)

df['ADJUSTED'] = pd.to_numeric(df['ADJUSTED'].replace(',', '', regex=True), errors='coerce')


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
    total_ADJUSTED = team['ADJUSTED'].sum()
    avg_ADJUSTED = team['ADJUSTED'].mean()
    print(f"Team {i+1}:")
    print(team[['PLAYER POOL', 'MAIN ROLE', 'ADJUSTED']])
    print(f"Average ADJUSTED: {avg_ADJUSTED}\n")
    print(f"Total ADJUSTED: {total_ADJUSTED}\n")
    print("\n")

















# # Declare team size
# team_size = 5

# # Calculate the number of teams of 5 given the general player count
# num_teams = len(df) // team_size

# # Split the dataframe into teams
# teams = [df.iloc[i:i+team_size] for i in range(0, len(df), team_size)]

# # Calculate average 'ADJUSTED' value for each team
# for i, team in enumerate(teams):
#     avg_ADJUSTED = team['ADJUSTED'].mean()
#     print(f"Team {i+1}:")
#     print(team[['PLAYER POOL', 'ADJUSTED']])
#     print(f"Average ADJUSTED: {avg_ADJUSTED}\n")