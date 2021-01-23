import sys


def hanoi(n: int, start: int, by: int, end: int) -> None:
    if n == 1:
        move.append([start, end])
    else:
        hanoi(n - 1, start, end, by)
        move.append([start, end])
        hanoi(n - 1, by, start, end)


n = int(sys.stdin.readline())
move = []
hanoi(n, 1, 2, 3)
print(len(move))
print("\n".join([" ".join(str(i) for i in row) for row in move]))
