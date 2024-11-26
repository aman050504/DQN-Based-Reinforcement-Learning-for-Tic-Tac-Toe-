import importlib
import random
import os
from TicTacToe import *


def play_full_game(playerSQN, smartness):
    """Plays a full game of TicTacToe and returns the result (win/loss/draw)"""
    game = TicTacToe(smartness, playerSQN)
    game.play_game()
    reward = game.get_reward()

    if reward == 1:
        print("\033[32mPlayer 2 Wins\033[0m")
        return "win"
    elif reward == 0:
        print("\033[33mDraw\033[0m")
        return "draw"
    else:
        print("\033[31mPlayer 2 Loses\033[0m")
        return "loss"


def check(submission):
    """Checks the submission for all test cases"""

    # Dynamically import the module
    module_name = f"{submission}"
    my_module = importlib.import_module(module_name)

    # Results tracking
    results_smartness_0 = {"win": 0, "loss": 0, "draw": 0}
    results_smartness_0_8 = {"win": 0, "loss": 0, "draw": 0}

    # Testing for smartness = 0
    print("\n_____________Smartness 0_____________\n")
    for seed in range(1, 2001):
        random.seed(seed)
        playerSQN = my_module.PlayerSQN()
        print(f"Testing full game at smartness = 0, seed = {seed}")
        smartness = 0
        result = play_full_game(playerSQN, smartness)
        results_smartness_0[result] += 1
        del playerSQN

    # Testing for smartness = 0.8
    print("\n_____________Smartness 0.8_____________\n")
    for seed in range(1, 2001):
        random.seed(seed)
        playerSQN = my_module.PlayerSQN()
        print(f"Testing full game at smartness = 0.8, seed = {seed}")
        smartness = 0.8
        result = play_full_game(playerSQN, smartness)
        results_smartness_0_8[result] += 1
        del playerSQN

    # Print results
    print("\nResults for Smartness 0:")
    print(f"Wins: {results_smartness_0['win']}, Losses: {results_smartness_0['loss']}, Draws: {results_smartness_0['draw']}")
    print("\nResults for Smartness 0.8:")
    print(f"Wins: {results_smartness_0_8['win']}, Losses: {results_smartness_0_8['loss']}, Draws: {results_smartness_0_8['draw']}")


if __name__ == "__main__":
    # Get list of submissions
    current_directory = os.getcwd()
    files = [
        f
        for f in os.listdir(current_directory)
        if os.path.isfile(os.path.join(current_directory, f)) and f.startswith("20") and f.endswith(".py")
    ]

    for submission in files:
        check(submission[:-3])