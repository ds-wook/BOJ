# 2631 줄세우기
from typing import List

N = int(input())
children = [int(input()) for _ in range(N)]


def lis(arr: List[int]) -> int:
    MAX = 0
    dp = [0 for _ in range(N)]
    dp[0] = 1
    for i in range(1, N):
        for j in range(0, i):
            if arr[i] > arr[j]:
                MAX = max(MAX, dp[j])
        dp[i] = MAX + 1
        MAX = 0

    return max(dp)


print(N - lis(children))
