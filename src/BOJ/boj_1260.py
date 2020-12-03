from typing import Dict, Set
from collections import deque
import sys

graph = {}
node, edge, start = map(int, sys.stdin.readline().split())
for i in range(edge):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 not in graph:
        graph[n1] = set([n2])
    elif n2 not in graph[n1]:
        graph[n1].update([n2])
    if n2 not in graph:
        graph[n2] = set([n1])
    elif n1 not in graph[n2]:
        graph[n2].update([n1])


def dfs(graph: Dict[int, Set[int]], root: int) -> str:
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                push = sorted(list(set(graph[n]) - set(visited)), reverse=True)
                stack += push
    return ' '.join([str(v) for v in visited])


def bfs(graph: Dict[int, Set[int]], root: int) -> str:
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                push = sorted(list(set(graph[n]) - set(visited)))
                queue += push
    return ' '.join([str(v) for v in visited])


print(dfs(graph, start))
print(bfs(graph, start))
