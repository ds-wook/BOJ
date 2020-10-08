# 1300 K번째 수
N = int(input())
K = int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, N + 1):
        count += min(mid // i, N)

    if count >= K:
        answer = mid
        end = mid - 1

    else:
        start = mid + 1
        print(answer)
