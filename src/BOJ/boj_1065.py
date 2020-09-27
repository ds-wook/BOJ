# 1065 한수
N = int(input())


def hanNumber(N: int) -> int:
    han = 0
    for n in range(1, N + 1):
        if n < 100:
            han += 1
        else:
            n = str(n)
            if int(n[1]) == (int(n[0]) + int(n[-1])) / 2:
                han += 1
    return han


print(hanNumber(N))
