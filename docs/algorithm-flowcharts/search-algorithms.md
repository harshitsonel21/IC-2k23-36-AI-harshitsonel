# Search Algorithms Flow (text form)

1. Start with an initial state and goal test.
2. Select a frontier policy:
   - BFS: FIFO queue.
   - DFS: LIFO stack.
   - Best First: lowest heuristic value first.
   - A*: lowest `g(n) + h(n)` first.
3. Remove a state from the frontier.
4. If it is the goal, reconstruct and return the path.
5. Otherwise expand valid unvisited neighbours and add them to the frontier.
6. Stop when the frontier is empty (no solution).
