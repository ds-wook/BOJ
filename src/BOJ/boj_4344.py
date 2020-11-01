import sys

line = int(sys.stdin.readline())

for _ in range(line):
    number = list(map(int, sys.stdin.readline().split()))
    scores = [n for n in number[1:]]
    average = sum(scores) / len(scores)
    count = 0
    for score in scores:
        if average < score:
            count += 1
    print(f'{(count / number[0]) * 100:.3f}%')
