# 2991 사나운 개
A, B, C, D = map(int, input().split())
delivery = list(map(int, input().split()))

for i in delivery:
    dog = 0
    if i % (A + B) > 0 and i % (A + B) <= A:
        dog += 1
    if i % (C + D) > 0 and i % (C + D) <= C:
        dog += 1
    print(dog)