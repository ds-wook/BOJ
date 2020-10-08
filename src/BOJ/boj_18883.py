# 18883 N M 출력
n, m = [int(i) for i in input().split()]

list_number = [i for i in range(1, n * m + 1)]

for i, n in enumerate(list_number):
    if i % m == m - 1:
        print(n)
    else:
        print(n, end=" ")
