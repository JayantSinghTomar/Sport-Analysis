import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample Data (Replace with actual data)
data = {
    "Team": [
        "South Africa", "India", "West Indies", "Afghanistan", "Australia", "England", 
        "No Result", "Bangladesh", "Scotland", "Pakistan", "New Zealand",
        "USA", "Netherlands", "Uganda", "Canada", "Sri Lanka"
    ],
    "Matches": [10, 10, 8, 7, 7, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3],  # Total matches played
    "Wins": [8, 8, 5, 5, 5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1]  # Wins achieved
}

# Convert to DataFrame and Calculate Win Percentage
df = pd.DataFrame(data)
df["Win %"] = round((df["Wins"] / df["Matches"]) * 100, 1)

# Sort Data by Wins
df = df.sort_values(by="Wins", ascending=True)

# Define Colors (Gradient Effect)
colors = plt.cm.viridis(np.linspace(0.2, 1, len(df)))

# Create Figure (Reduced Width)
fig, ax = plt.subplots(figsize=(10, 7))  # Reduced width

# 3D Effect - Shadow bars
ax.barh(df["Team"], df["Wins"], color="gray", edgecolor="black", alpha=0.3)

# Main Bars with Gradient Colors
bars = ax.barh(df["Team"], df["Wins"], color=colors, edgecolor="black", alpha=0.9)

# Titles and Labels (Georgia Font, Small Size)
ax.set_title("Match Wins by Team", fontsize=14, fontname="Georgia", pad=10)
ax.set_xlabel("Number of Wins", fontsize=12, fontname="Georgia")
ax.set_ylabel("Teams", fontsize=12, fontname="Georgia")

# Create Legend-like Box at Right Side
fig.subplots_adjust(right=0.8)  # Adjust space for the labels on the right side
for i, (team, matches, wins, color) in enumerate(zip(df["Team"], df["Matches"], df["Wins"], colors)):
    plt.gcf().text(0.82, 0.15 + i * 0.03, f" ", bbox=dict(facecolor=color, edgecolor='black', boxstyle='square,pad=0.3'))
    plt.gcf().text(0.84, 0.15 + i * 0.03, f"{team} - {wins}/{matches}", fontsize=10, fontname="Georgia", verticalalignment="center")

# Annotate Data Points with Team Names Inside Bars
for bar, team in zip(bars, df["Team"]):
    ax.text(bar.get_width() / 2, bar.get_y() + bar.get_height()/2, team,
            ha='center', va='center', fontsize=10, fontname="Georgia", color="black", fontweight="bold")

# Improve Readability
ax.set_yticks(range(len(df)))  # Set fixed tick positions
ax.set_yticklabels(["" for _ in df["Team"]])  # Remove default labels
plt.grid(axis="x", linestyle="--", alpha=0.7)
ax.spines['left'].set_visible(False)  # Remove left-side grid line

# Show Plot
plt.show()
