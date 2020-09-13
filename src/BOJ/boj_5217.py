# 5217 쌍의 합
for _ in range(int(input())):
    n = int(input())
    print(f'Pairs for {n} : {", ".join([f"{i} {n - i}" for i in range(1, n // 2 + (1 if n % 2 else 0))])}')