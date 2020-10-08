# 2675 문자열 반복
line = int(input())
for _ in range(line):
    n, string = [s for s in input().split()]
    answer = "".join([int(n) * s for s in string])
    print(answer)
