from typing import Dict, Set
from collections import deque
import sys

node, edge, start = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, node+1)}

for i in range(1, edge + 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for key in graph:
    graph[key].sort()


def dfs(graph: Dict[int, Set[int]], root: int) -> str:
    visited = {}
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.setdefault(n)
            print(visited)
            stack += reversed(graph[n])
    return ' '.join([str(v) for v in visited])


def bfs(graph: Dict[int, Set[int]], root: int) -> str:
    visited = {}
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.setdefault(n)
            print(visited)
            queue += graph[n]
    return ' '.join([str(v) for v in visited])


print(dfs(graph, start))
print(bfs(graph, start))
