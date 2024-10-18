import pandas as pd
import numpy as np





# Define the rank distribution
rank_distribution = {
    'Iron': 12,
    'Bronze': 21,
    'Silver': 17,
    'Gold': 15,
    'Platinum': 16,
    'Emerald': 12,
    'Diamond': 4.1,
    'Master': 0.69,
    'GrandMaster': 0.062,
    'Challenger': 0.026
}

# Define a maximum points scale
max_points = 50

# Calculate points for each rank based on the distribution
rank_points = {}
for rank, percentage in rank_distribution.items():
    # Assign points inversely proportional to the percentage (higher percentage gets more points)
    rank_points[rank] = max_points * (percentage / sum(rank_distribution.values()))

# Display the points assigned to each rank
for rank, points in rank_points.items():
    print(f"{rank}: {points:.2f} points")
