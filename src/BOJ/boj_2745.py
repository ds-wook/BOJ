# 2745 진법변환
codes = {c: i for i, c in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
N, B = input().split()
B = int(B)
result = sum([codes[n] * (B ** i) for i, n in enumerate(N[::-1])])
print(result)
