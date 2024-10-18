# Team Balance Scripts

These scripts were written to test the quality of adjusted points and flat points as elo indicators to balance teams for the Winter Righteous Glory League of legends tournament. They read player data from a CSV file, processes the data to remove unwanted entries, and assigns players to balanced teams based on their main roles and points. It uses the Pandas library for data manipulation and NumPy for numerical operations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Functionality](#functionality)


## Installation

To run this script, ensure you have Python installed on your machine. You will also need to install the required libraries:

```bash
pip install pandas numpy
```
## Usage
1. Place your CSV file (RG_WNTR Invitational - Sheet2.csv) in the same directory as this script.
2. Run the script using the following command:

```bash
python team_assignment.py
```
3. The output will display the assigned teams along with their average and total points.

## Data
- PLAYER POOL: The name of the player
- ROLES: Initials to indicate playable roles
- MAIN ROLE: The prefered role of the player
- 50 GAMES?: Boolean value for if the player has played up to 50 ranked games this season
- 2024 PEAK: The peak rank of the player in season 14
- ALL TIME PEAK: The all-time peak of the player
- AVG PING: The average ping of the player
- PING SPIKES: The frequency of team spikes
- PRACTICE:
- POINTS:
- ADJUSTED:

  ## Functionality
1. Data Loading: The script loads player data from a CSV file.
2. Data Cleaning: Converts the 50 GAMES? column to boolean values. Removes rows where POINTS is marked as '-'.
3. Data Shuffling: Randomly shuffles the dataframe to ensure fair team assignments.
4. Team Creation: Groups players by their main roles, determines the minimum number of players available in any role to balance team sizes, creates teams by selecting one player from each role until all roles are exhausted.
5. Output: Prints each team's members along with their total and average points.


  ## Contributing
  Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or bugs.
  
