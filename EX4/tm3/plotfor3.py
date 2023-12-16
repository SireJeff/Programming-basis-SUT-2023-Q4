import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Initialize empty lists to store data
game_iterations = []
player1_scores = []
player2_scores = []
player1_healths = []
player2_healths = []

# Open and read the text file
with open('result.txt', 'r') as file:
    # Split the content into individual game sections
    game_sections = file.read().split('------------------------------------------\n')

    # Iterate through each game section
    for section in game_sections:
        # Split the section into lines
        lines = section.strip().split('\n')

        # Extract game iteration number
        game_iteration = int(lines[0].split('=')[1])

        # Extract player scores and healths
        player1_score = int(lines[1].split(':')[1].split(',')[0].strip())
        player1_health = int(lines[1].split(':')[2].strip())
        
        player2_score = int(lines[2].split(':')[1].split(',')[0].strip())
        player2_health = int(lines[2].split(':')[2].strip())

        # Append the data to respective lists
        game_iterations.append(game_iteration)
        player1_scores.append(player1_score)
        player2_scores.append(player2_score)
        player1_healths.append(player1_health)
        player2_healths.append(player2_health)

# Print the gathered data
print("Game Iterations:", game_iterations)
print("Player 1 Scores:", player1_scores)
print("Player 2 Scores:", player2_scores)
print("Player 1 Healths:", player1_healths)
print("Player 2 Healths:", player2_healths)

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'Game Iteration': game_iterations,
    'Player1 Score': player1_scores,
    'Player1 Health': player1_healths,
    'Player2 Score': player2_scores,
    'Player2 Health': player2_healths
})

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

# Plot scores over game iterations
plt.subplot(1, 2, 1)
sns.lineplot(data=df, x='Game Iteration', y='Player1 Score', label='Player1')
sns.lineplot(data=df, x='Game Iteration', y='Player2 Score', label='Player2')
plt.title('Player Scores Over Game Iterations')
plt.xlabel('Game Iteration')
plt.ylabel('Score')

# Plot health over game iterations
plt.subplot(1, 2, 2)
sns.lineplot(data=df, x='Game Iteration', y='Player1 Health', label='Player1')
sns.lineplot(data=df, x='Game Iteration', y='Player2 Health', label='Player2')
plt.title('Player Health Over Game Iterations')
plt.xlabel('Game Iteration')
plt.ylabel('Health')

plt.tight_layout()
plt.show()
