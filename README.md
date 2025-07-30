# Deep Q-Network for Tic-Tac-Toe

This project implements a **Deep Q-Network (DQN)** for playing the classic game **Tic-Tac-Toe** using **Reinforcement Learning (RL)**. The agent learns optimal strategies through trial and error by interacting with the game environment and adjusting its behavior based on rewards.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Results and Evaluation](#results-and-evaluation)
- [License](#license)

## Project Overview
This project demonstrates the use of **Deep Q-Networks** to train an agent to play Tic-Tac-Toe. The agent uses **Q-learning**, a type of reinforcement learning, to decide the best actions at each step of the game. The neural network helps the agent learn from the experience replay buffer and improve its performance over time.

## Requirements
To run the project, you'll need the following:

- Python 3.8 or later  
- TensorFlow  
- Keras  
- NumPy  
- Matplotlib (for visualization)  
- **Flask** (for the web interface)  
- A Python-compatible IDE (e.g., PyCharm, Visual Studio Code)  

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shallow-q-network-tic-tac-toe.git
   cd shallow-q-network-tic-tac-toe
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the correct versions of Python and the libraries mentioned.

## Usage

To **train the agent**, run the following command:
```bash
python train.py
```

To **evaluate the agent’s performance** after training, run:
```bash
python evaluate.py
```
This will play the agent against a random player and report the performance.

To **play against the AI in your web browser**, start the Flask server:
```bash
python app.py
```
After running the command, open your browser and navigate to the address shown in the terminal, which is typically:
```
http://127.0.0.1:5001
```

## How It Works

- **Experience Replay**: The agent uses an experience replay buffer to store states, actions, rewards, and next states, which helps improve training stability.

- **Epsilon-Greedy Policy**: The agent initially explores the environment with a high degree of randomness (exploration) and then gradually exploits the learned knowledge (exploitation) by adjusting the epsilon value.

- **Neural Network Architecture**:  
  The neural network has 2 hidden layers with 64 neurons each and uses ReLU activations. The output layer has 9 units, representing the Q-values for each of the 9 possible moves in Tic-Tac-Toe.

- **Training**:  
  The agent plays multiple games and learns by minimizing the error between the predicted Q-values and the target Q-values calculated using the Bellman equation.

## Results and Evaluation

- **Training**:  
  The agent was trained over thousands of episodes using the epsilon-greedy strategy, and its performance improved gradually over time.

- **Performance Evaluation**:  
  After training, the agent was evaluated against both random and more skilled players. Graphs depicting the win rate over training episodes show how the agent’s performance improves as training progresses.

### Key Findings:
- The agent successfully learned optimal strategies to play Tic-Tac-Toe.
- The model's performance improved with the decrease in exploration (epsilon) over time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
