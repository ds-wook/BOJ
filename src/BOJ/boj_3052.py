# 3052 나머지
rest = [int(input()) % 42 for _ in range(10)]
rest = set(rest)
answer = len(rest)
print(answer)