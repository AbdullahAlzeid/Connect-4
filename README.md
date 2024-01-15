# Connect-4

 ![Alt text](/images/con4.png)

## Overview
Connect-4 is a popular two-player connection game where players choose a color and take turns dropping colored discs into a grid. The goal is to form a line of four discs.

## Repository Structure
- **Agents**: AI agents with different strategies.
  - [AgentA.py](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Agents/AgentA.py): Minimax algorithm with Alpha-Beta pruning.
  - [AgentB.py](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Agents/AgentB.py): Expectimax algorithm with Alpha-Beta pruning.
  - [AgentC.py](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Agents/AgentC.py): Random move selection.
- **Heuristics**: 
  - [Heuristics.py](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Heuristics/Heuristics.py): Heuristic function for AI decision-making.
- **Main**: 
  - [Driver.py](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Main/Driver.py): Main script for running simulations.
- **Puzzle Representation**: 
  - [Connect4.py](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Puzzle%20Representation/Connect4.py): Game logic.
- **Report**: 
  - [ICS381-Assignment 3.pdf](https://github.com/AbdullahAlzeid/Connect-4/blob/main/Report/ICS381-Assignment%203.pdf)

## How to Run
1. Navigate to `Main`.
2. Run `Driver.py`.

## AI Agents
- **AgentA**: Minimax with Alpha-Beta pruning.
- **AgentB**: Expectimax with Alpha-Beta pruning.
- **AgentC**: Random moves.

## Heuristics
Evaluates the board, favoring winning positions and blocking opponent's moves.

## Game Simulation
`Driver.py` simulates games, logs moves, and provides statistics. Any two agents can be picked to play against each other and provide statistical summaries about the results of the games

## License
Licensed under the [MIT License](https://github.com/AbdullahAlzeid/Connect-4/blob/main/LICENSE).
