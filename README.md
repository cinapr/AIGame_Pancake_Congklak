# Artificial Intelligence - Agents and Infrastructure

First assignment of **Course 1.5: Artificial Intelligence – 6 ECTS** : Make 2 game; 1st is one player; 2nd is two players game

This repository contains the implementation for Homework 1 of the "Artificial Intelligence 2022: Agents and Infrastructure" course. The assignment focuses on developing a modular infrastructure to run simulations of agents using various heuristic search algorithms, applied to selected puzzles and games.

---

## Project Overview

### **Task Questions**
Artificial Intelligence 2022

Agent and Infrastructure implementation
Homework 1 assigned 18/10/2022 due 28/10/21
(Recommended: on a python jupyter notebook)

Implement "Infastructure" the main() that runs the "simulation" of the agents

Agent acting in the world:
State/world-situation representation
main(S(t), A(t))=S(t+1);
main(S(t)) (loop(for i: A.(t)=action(Agent,S(t));

S(t+1) for i: apply action A.(t) on S(t)}}
Implement agents that use the various Heuristic Search Algorithms...
Instantiate your infrastructure with a single agent to solve a puzzle of your choice (no TICТАСТОЕ...)
Write a report describing your implementations and a statistics over sample runs.
Your statistic should compare the performance of different agents running different Search Algo and/or different heuristic evaluations

Instantiate your infrastructure with two agents to play a board game (recommended chess)
tas before main(S(t), A(t))-5(t+1); but now agent1 does nothing when t-even and plays a move when twodd, and viceversa for agent2..

Instructions and recommendations:
1. Keep your implementation as modular as possible, keeping various components (infrastructure, state representation and computation of agent actions effects, agents, search algo, Heuristic functions...) well separated from each other and/or encapsulated...
For example, it should be possible, given an implementation that plays chess. to use it to play a different game by simply changing the game model (representation and functions).

2. You can import existing libraries or other implementations (clearly state. when you do so. your source) as long as you clearly distinguish what you have imported from what you have created yourself.
Grading will highly depend on how smart is the modularity of your Implementation and will consider the originality abovej of what you turn in (see point 2



### **Part 1: Pancake Puzzle**
Implemented a single-agent infrastructure where the agent solves the **Pancake Sorting Puzzle** using heuristic search algorithms. The Pancake Puzzle involves flipping segments of a stack of pancakes to sort them by size, with the smallest pancake on top.

- **Features:**
  - State representation: Pancake stack as a list of integers.
  - Heuristic algorithms implemented:
    - Breadth-First Search (BFS)
    - A* Search with heuristic functions (e.g., the largest misplaced pancake distance).
  - Comparative performance analysis of algorithms over multiple runs.

### **Part 2: Congklak Game**
Developed a two-agent infrastructure where agents play the traditional **Congklak (Mancala)** board game in a turn-based fashion.

- **Features:**
  - Two-agent turn-based game structure.
  - Game state representation includes pit states and player scores.
  - Algorithms:
    - Minimax with Alpha-Beta Pruning
    - Brute Force
  - Comparative performance analysis of agents using different search strategies.

---

## Installation and Running

1. Pull the project
2. Open folder **Jupyter-Notebook and Imported Classes Code** with Jupyter Notebook 
3. Run **Main.ipynb**


