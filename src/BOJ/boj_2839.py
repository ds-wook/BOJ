# 2839 설탕 배달
N = int(input())
kg_list = [x + y for x in range(1000 + 1) for y in range(1000 + 1) if 5 * x + 3 * y == N]
countMin = min(kg_list) if kg_list != [] else -1
print(countMin)