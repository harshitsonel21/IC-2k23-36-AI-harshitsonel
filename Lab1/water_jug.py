"""Solve the classic two-jug problem using breadth-first search."""
from collections import deque

def solve(cap_a=4, cap_b=3, target=2):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path
        next_states = {
            (cap_a, b), (a, cap_b), (0, b), (a, 0),
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),
            (a + min(b, cap_a - a), b - min(b, cap_a - a)),
        }
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

if __name__ == "__main__":
    result = solve()
    print("State sequence (jug A, jug B):")
    print(result if result else "No solution")
