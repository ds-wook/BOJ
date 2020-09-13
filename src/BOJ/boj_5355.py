# 5355 화성수학
line = int(input())
for _ in range(line):
    calculate = [s for s in input().split()]
    answer = 0.0
    for i, op in enumerate(mars):
        if i == 0:
            answer += float(op)
        else:
            if op == '#':
                answer -= 7
            elif op == '%':
                answer += 5
            elif op == '@':
                answer *= 3
    print(f'{number:.2f}')