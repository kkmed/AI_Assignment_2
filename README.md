# Pathfinding Algorithms: Dijkstra, A* and Dynamic Replanning

## Overview

This project explores different pathfinding strategies across **static and dynamic environments**:

1. **Dijkstra’s Algorithm** – Shortest path in a weighted graph (city network)
2. **A\* Algorithm** – Efficient shortest path in a static grid with obstacles
3. **Dynamic Path Planning (Repeated A\*)** – Navigation in environments with unknown and changing obstacles

The project demonstrates how pathfinding evolves from:
> Static → Heuristic → Adaptive systems

---

# 1. Dijkstra’s Algorithm (Graph-Based Shortest Path)

## Problem
Find the shortest distance between two cities using a dataset of city-to-city distances.

## Approach
- Graph constructed using an adjacency list from CSV data
- Uses a **min-heap (priority queue)** for efficiency
- Maintains:
  - `distances` → shortest distance from source
  - `prev` → parent tracking for path reconstruction

## Features
- Works on **weighted graphs**
- No heuristic used
- Guarantees globally optimal shortest path

## Output
- Minimum distance between cities
- Path (sequence of cities)

# 2. A* Algorithm (Static Grid Navigation)

## Problem
Find the shortest path in a **70×70 grid** with obstacles.

- `0` → free cell  
- `1` → obstacle  

## Approach

A* uses:
f(n) = g(n) + h(n)

- `g(n)` → actual cost from start  
- `h(n)` → Manhattan distance to goal (heuristic)

## Features
- Priority queue based on `f(n)`
- Uses `g_score` to track best paths
- Backtracking for path reconstruction

## Measures of Effectiveness (A*)

### Path Length
- Number of steps from start to goal  
- Represents optimality of solution  

### Nodes Explored
- Number of nodes expanded  
- Indicates efficiency  

### Computation Time
- Time taken to compute path  
- Increases with obstacle density  

### Optimality
- Guaranteed due to **admissible heuristic (Manhattan distance)**  

## Observations
- Low density → faster execution, fewer nodes explored  
- High density → more computation required  
- A* outperforms Dijkstra due to heuristic guidance  

# 3. Dynamic Path Planning (Repeated A* Replanning)

## Problem
Navigate a grid where:
- Obstacles are **not fully known initially**
- Obstacles can **change dynamically over time**

## Key Idea

Instead of computing a single path:

> Plan → Move → Observe → Replan

## Approach

### Two Grids:
- `actual_grid` → real environment (dynamic and hidden)
- `known_grid` → robot’s knowledge (updated during movement)

### Execution Loop:
1. Compute path using A* on `known_grid`  
2. Move one step along the path  
3. Update environment (dynamic obstacle changes)  
4. Reveal nearby cells to the robot  
5. Recompute path if necessary  

## Important Note

This implementation uses **repeated A\*** for replanning.

- It is **not a full D\* or D\* Lite algorithm**
- It recomputes paths from scratch instead of updating incrementally

However, it captures the core idea of:
> **adaptive navigation in dynamic environments**

## Output

- **Trajectory** → actual path taken by the robot  
- **Steps** → total movement cost  
- **Replans** → number of times path was recomputed  
- **Status** → success or failure  

## Measures of Effectiveness (Dynamic Case)

### Trajectory Length
- Actual distance traveled  
- May be longer than optimal due to changes  

### Number of Replans
- Indicates how often environment disrupts planning  

### Success Rate
- Whether the robot reaches the goal  

### Adaptability
- Ability to adjust to new obstacles  

## Observations

- Higher obstacle density → more replanning required  
- Dynamic changes → longer trajectories  
- Path optimality is **not guaranteed globally**  
- In highly unstable environments, the goal may become unreachable  

# Algorithm Comparison

| Feature | Dijkstra | A* | Dynamic (Repeated A*) |
|--------|--------|----|------------------------|
| Environment | Static Graph | Static Grid | Dynamic Grid |
| Heuristic | No | Yes | No |
| Replanning | No | No | Yes |
| Optimal Path | Yes | Yes | Not guaranteed |
| Efficiency | Moderate | High | Depends on environment |

# Key Insights

- **Dijkstra**: Reliable but uninformed search  
- **A\***: Efficient due to heuristic guidance  
- **Dynamic replanning**: Necessary when environment is unknown or changing  

In dynamic systems:
> Global optimality is less important than adaptability

# How to Run

## Dijkstra
- python dijkstra.py
## A*
- python a_star.py
## Dynamic Replanning
- python d_star.py

# Conclusion

This project highlights the evolution of pathfinding algorithms:

> From finding shortest paths → to adapting in uncertain environments

- Static algorithms assume complete knowledge  
- Real-world systems must handle **uncertainty and change**

# Future Improvements

- Implement **D\* Lite** for efficient incremental replanning  
- Add grid visualization  
- Optimize performance for larger environments  
