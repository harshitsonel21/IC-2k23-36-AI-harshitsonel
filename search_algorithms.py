"""BFS, DFS, Greedy Best-First Search and A* on a small weighted graph."""
from collections import deque
import heapq
import time

GRAPH = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 2)],
    "D": [("G", 5)],
    "E": [("G", 1)],
    "F": [("G", 3)],
    "G": [],
}
H = {"A": 7, "B": 6, "C": 4, "D": 4, "E": 1, "F": 2, "G": 0}

def bfs(start, goal):
    q, seen = deque([(start, [start])]), {start}
    while q:
        node, path = q.popleft()
        if node == goal: return path
        for nxt, _ in GRAPH[node]:
            if nxt not in seen:
                seen.add(nxt); q.append((nxt, path + [nxt]))
    return None

def dfs(start, goal):
    stack, seen = [(start, [start])], set()
    while stack:
        node, path = stack.pop()
        if node == goal: return path
        if node in seen: continue
        seen.add(node)
        for nxt, _ in reversed(GRAPH[node]):
            if nxt not in seen: stack.append((nxt, path + [nxt]))
    return None

def best_first(start, goal):
    heap, seen = [(H[start], start, [start])], set()
    while heap:
        _, node, path = heapq.heappop(heap)
        if node == goal: return path
        if node in seen: continue
        seen.add(node)
        for nxt, _ in GRAPH[node]:
            if nxt not in seen: heapq.heappush(heap, (H[nxt], nxt, path + [nxt]))
    return None

def astar(start, goal):
    heap, best = [(H[start], 0, start, [start])], {start: 0}
    while heap:
        _, cost, node, path = heapq.heappop(heap)
        if node == goal: return path, cost
        if cost != best[node]: continue
        for nxt, weight in GRAPH[node]:
            new_cost = cost + weight
            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heapq.heappush(heap, (new_cost + H[nxt], new_cost, nxt, path + [nxt]))
    return None, float("inf")

if __name__ == "__main__":
    for name, fn in [("BFS", bfs), ("DFS", dfs), ("Best First", best_first)]:
        t0 = time.perf_counter(); path = fn("A", "G"); elapsed = time.perf_counter() - t0
        print(f"{name}: path={path}, time={elapsed:.8f}s")
    t0 = time.perf_counter(); path, cost = astar("A", "G"); elapsed = time.perf_counter() - t0
    print(f"A*: path={path}, cost={cost}, time={elapsed:.8f}s")
