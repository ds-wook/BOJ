from typing import Dict, List
from collections import deque
import sys


def make_graph(node: int, edge: int) -> Dict[int, List[int]]:
    graph = {i: [] for i in range(1, node+1)}
    for i in range(1, edge + 1):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for key in graph:
        graph[key].sort()

    return graph


def dfs(graph: Dict[int, List[int]], root: int) -> str:
    visited = {}
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.setdefault(n)
            stack += reversed(graph[n])
    return ' '.join([str(v) for v in visited])


def bfs(graph: Dict[int, List[int]], root: int) -> str:
    visited = {}
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.setdefault(n)
            queue += graph[n]
    return ' '.join([str(v) for v in visited])


if __name__ == "__main__":
    node, edge, start = map(int, sys.stdin.readline().split())
    graph = make_graph(node, edge)
    print(dfs(graph, start))
    print(bfs(graph, start))
