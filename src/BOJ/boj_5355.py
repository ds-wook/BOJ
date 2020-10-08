# 5355 화성수학
import sys

line = int(sys.stdin.readline())
for _ in range(line):
    calculate = [s for s in sys.stdin.readline().split()]
    answer = 0.0
    for i, op in enumerate(calculate):
        if i == 0:
            answer += float(op)
        else:
            if op == '#':
                answer -= 7
            elif op == '%':
                answer += 5
            elif op == '@':
                answer *= 3
    print(f'{answer:.2f}')
