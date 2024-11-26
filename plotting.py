import json
import matplotlib.pyplot as plt
import numpy as np


def plot_win_rate_and_running_avg(json_file, win_rate_file="win_rate_plot.png", running_avg_file="running_avg.png", games_per_score=20):
    """
    Plots the win rate and running average of scores over time based on data in a JSON file.

    Parameters:
    - json_file (str): Path to the JSON file containing the scores.
    - win_rate_file (str): Path to save the win rate plot image.
    - running_avg_file (str): Path to save the running average plot image.
    - games_per_score (int): Number of games corresponding to each score entry.
    """
    # Load data from the JSON file
    try:
        with open(json_file, 'r') as file:
            scores = json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return

    if not isinstance(scores, list) or len(scores) == 0:
        print("Invalid or empty data in the JSON file.")
        return

    # Calculate win rates (assuming each score corresponds to total reward for 20 games)
    win_rates = [(score / games_per_score + 1) / 2 for score in scores]  # Normalize score to win rate

    # Calculate running average of scores
    running_avg = np.cumsum(scores) / np.arange(1, len(scores) + 1)

    # Plot the win rate
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(win_rates) + 1), win_rates, label="Win Rate", color="blue", linewidth=2)
    plt.axhline(y=0.5, color='red', linestyle='--', label="Baseline Win Rate (50%)")
    plt.title("Performance Improvement Over Training Episodes", fontsize=16)
    plt.xlabel("Scores (Batch Count)", fontsize=14)
    plt.ylabel("Win Rate", fontsize=14)
    plt.ylim(0, 1)  # Win rate is between 0 and 1
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    plt.tight_layout()

    # Save the win rate plot
    plt.savefig(win_rate_file)
    print(f"Win rate plot saved as {win_rate_file}")
    plt.close()

    # Plot the running average
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(running_avg) + 1), running_avg, label="Running Average", color="green", linewidth=2)
    plt.title("Running Average of Scores Over Training Episodes", fontsize=16)
    plt.xlabel("Training Batches", fontsize=14)
    plt.ylabel("Running Average of Scores", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=12)
    plt.tight_layout()

    # Save the running average plot
    plt.savefig(running_avg_file)
    print(f"Running average plot saved as {running_avg_file}")
    plt.close()


# Example usage
if __name__ == "__main__":
    json_file = "win_percentage_0.5.json"  # Replace with your JSON file path
    win_rate_file = "win_rate_0.5_plot.png"  # Output file for the win rate plot
    running_avg_file = "running_avg_0.5_plot.png"  # Output file for the running average plot
    games_per_score = 20  # Number of games per score entry

    plot_win_rate_and_running_avg(json_file, win_rate_file, running_avg_file, games_per_score)
