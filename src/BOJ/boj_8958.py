# 8958 OX퀴즈
line = int(input())
for _ in range(line):
    oxstring = input().split("X")
    oxlist = [[o for o in ox] for ox in oxstring]
    answer = sum([i + 1 for ox in oxlist for i, o in enumerate(ox)])
    print(answer)
