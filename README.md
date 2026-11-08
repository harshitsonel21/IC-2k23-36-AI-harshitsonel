Artificial Intelligence Laboratory

Student Name : HARSHIT SONEL

Roll Number : IC-2K23-36

Course : MCA

Semester : 7

Unified Readme File for All Programs Created in this Repo
This Repo is result of our 7th Semester Lab Work , and can be used as reference for revision purpose . This ReadMe contained all readme files from different folders Unit Wise for Quick and Easy Revision.

Unit 1: AI Problem Formulation & Intelligent Problem Solving

1. Vacuum Cleaner Problem
Problem Statement
A simple reflex agent cleans an environment consisting of two rooms (A and B). Each room can be either Clean or Dirty.

Production Rules
Rule 1 (Cleaning): If current room is Dirty 
→
 Action: SUCK.

Rule 2 (Movement A 
→
 B): If current room is A and Clean 
→
 Action: Move RIGHT.

Rule 3 (Movement B 
→
 A): If current room is B and Clean 
→
 Action: Move LEFT.

Learning Takeaways
Demonstrates a pure reflex agent: actions depend solely on the current percept, requiring no past memory.
Ideal for closed, fully observable, static


2. Water Jug Problem
   
Problem Statement

Given two jugs of capacities

X and Y with no measurement markings, measure exactly Z liters of water.

Solvability ConditionZ≤max(X,Y) and Z(modgcd(X,Y))=0

Intuitive Rule Loop

If Jug 1 is empty, fill it.

If Jug 2 is full, empty it.
Otherwise, pour water from Jug 1 into Jug 2 until Jug 2 is full or Jug 1 is exhausted.

Learning Takeaways
Demonstrates deterministic state manipulation where infinite capacity sources and sinks reduce continuous math to discrete

3. Missionaries and Cannibals Problem
Problem Statement
Three missionaries and three cannibals must cross a river using a two-person boat. At no point on either riverbank may cannibals outnumber missionaries (otherwise, missionaries are eaten).

State Representation
State: (M_left, C_left, boat)
M_left: Missionaries on the starting bank (0≤Mleft≤3)

C_left: Cannibals on the starting bank (0≤Clet≤3)

Start State: (3, 3, 1)
Goal State: (0, 0, 0)

For both sides of the river: If M>0⟹M≥C

Learning Takeaways

Introduces state constraints and pruning: states that violate safety are discarded immediately.
Breadth-First Search (BFS) guarantees discovering 


4. Rule-Based Decision Making
   
Problem Statement

An automated rule engine checks input symptoms/indicators against pre-programmed IF-THEN rules to classify a condition or issue recommendations.

Working Principle

Knowledge Base: Stores facts and rules.

Inference Engine: Evaluates inputs, tests rule criteria, and triggers actions/conclusions (forward chaining).

Learning Takeaways

Basis of classical expert systems: cleanly separates domain knowledge from the execution engine.

Quick Reference Summary

Experiment	Paradigm	State Representation	Goal Condition	Key Mechanism

1. Vacuum Cleaner	Production System	(Location, Status_A, Status_B)	Both rooms are Clean	Condition-Action Rules (Reflex agent)
2. Water Jug	State Simulation	(jug1_amt, jug2_amt)	jug1 == target or jug2 == target	Pour / Fill / Empty cycle
3. Missionaries & Cannibals	Constrained Search (BFS)	(M_left, C_left, Boat_pos)	(0, 0, 0)	Valid transitions where M≥C or M=0
4. Rule-Based Decision Making	Production System / Expert System	Fact dictionary / Set	Matching condition triggers recommendation	Forward-chaining pattern match

Unit 2: Heuristic Search Algorithms

1. Maze Solver (BFS)
   
Problem Formulation
Given a 2D grid where 0 is a walkable tile and 1 is an obstacle wall, find the shortest escape path from a start coordinate to an end coordinate.

Algorithm
Enqueue the initial position path: [(start_r, start_c)].
Pop the front path. Inspect the endpoint.
Check 4-directional moves (Up, Down, Left, Right).
If a neighbor is inside grid bounds, not a wall (0), and unvisited, enqueue path + [neighbor].
Repeat until the destination coordinate is popped.

2. Graph Traversal (DFS)
   
Problem Formulation
Explore deeply down each branch before backtracking to uncover all connected nodes in an arbitrary graph.

Algorithm
Mark the current node as visited and record it.
For each adjacent neighbor:
If the neighbor has not been visited, recursively invoke DFS on it.
Backtrack once all branches from the current node are exhausted.

3. Route Planning (Greedy Best-First Search)
4. 
Problem Formulation
Find a route between cities using estimated remaining distance to the goal as a heuristic guide.

Evaluation Functionf(n)=h(n)h(n): Estimated straight-line distance (SLD) from city n to the target.
The algorithm expands whichever valid neighbor appears closest to the goal, disregarding accumulated travel cost g(n).

4. 8-Puzzle Problem (A∗ Search)Problem FormulationTransform an initial 3×3 sliding tile configuration into the goal state using the blank tile (0) moves.

Evaluation Functionf(n)=g(n)+h(n)g(n): Number of moves made from the start state (depth).h(n): Manhattan Distance sum ∑(|x1−x2|+|y1−y2|) for every misplaced tile

expands states with the lowest combined f(n)score first, ensuring

Quick Reference Summary

Experiment	Search Type	Frontier Structure	Evaluation Function f(n)
Optimality / Completeness

1. Maze Solver	Uninformed (BFS)	Queue (FIFO)	Number of steps	Optimal for unit step costs; Complete
2. Graph Traversal (DFS)	Uninformed (DFS)	Call Stack (LIFO)	Depth explored	Neither optimal nor complete in infinite spaces
3. Route Planning	Informed (Greedy)	Priority Queue	f(n)=h(n)(heuristic only)	Not guaranteed optimal; fast exploration
4. 8-Puzzle Solver	Informed (A∗)	Priority Queue	f(n)=g(n)+h(n)Optimal and complete if h(n)is admissible
