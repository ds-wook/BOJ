# 5014 스타트 링크
from collections import deque
from typing import Union

def bfs(
    F:int,
    S:int,
    G:int,
    U:int,
    D:int) -> Union[int, str]:
    q = deque([[S, 0]])
    visited = {S}

    while q:
        floor, count = q.popleft()
        if floor == G:
            return count
        if floor + U <= F and floor + U not in visited:
            q.append([floor + U, count + 1])
            visited.add(floor + U)
        if floor - D >= 1 and floor - D not in visited:
            q.append([floor - D, count + 1])
            visited.add(floor - D)
    
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))