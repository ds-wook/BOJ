# 9237 이장님 초대
tree = int(input())
treecomplete = sorted([int(i) for i in input().split()][:tree], reverse=True)
completedate = max([(i + 1) + n + 1 for i, n in enumerate(treecomplete)])
print(completedate)