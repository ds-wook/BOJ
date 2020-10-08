# 10818 최대값 최솟값
N = int(input())
numbers = [int(i) for i in input().split()][:N]
print(min(numbers), max(numbers))
