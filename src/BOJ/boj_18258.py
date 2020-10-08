import sys
from collections import deque
# python collections 모듈 deque로 구현하면 속도를 줄일 수 있음

line = int(sys.stdin.readline())
queue = deque([])

for _ in range(line):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(order[1])

    elif order[0] == 'pop':
        # del을 쓰면 리스트요소들이 재배열하는데 시간이 걸리므로 popleft로 구현
        result = queue.popleft() if queue else -1
        print(result)

    elif order[0] == 'size':
        print(len(queue))

    elif order[0] == 'empty':
        result = 1 if not queue else 0
        print(result)

    elif order[0] == 'front':
        result = queue[0] if queue else -1
        print(result)

    elif order[0] == 'back':
        result = queue[-1] if queue else -1
        print(result)
