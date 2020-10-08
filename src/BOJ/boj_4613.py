# 4613 QUICKSUM
codes = {c: i for i, c in enumerate(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
while True:
    massage = input()
    if massage == "#":
        break
    quicksum = sum([codes[n] * (i + 1) for i, n in enumerate(massage)])
    print(quicksum)
