import sys


class Stack:
    def __init__(self):
        self.list = []

    def push(self, num: str) -> None:
        self.list.append(num)

    def pop(self) -> int:
        if self.size() == 0:
            return -1
        pop_result = self.list[-1]
        del self.list[-1]
        return pop_result

    def size(self) -> int:
        return len(self.list)

    def empty(self) -> int:
        return 1 if not self.list else 0

    def top(self) -> int:
        return -1 if not self.list else self.list[-1]


line = int(sys.stdin.readline())
stack = Stack()
for _ in range(line):
    order = sys.stdin.readline()
    order = order.split()
    if order[0] == 'push':
        stack.push(int(order[1]))
    elif order[0] == 'pop':
        print(stack.pop())
    elif order[0] == 'size':
        print(stack.size())
    elif order[0] == 'empty':
        print(stack.empty())
    elif order[0] == 'top':
        print(stack.top())
    else:
        print('Wrong!!')
