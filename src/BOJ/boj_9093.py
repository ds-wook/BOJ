# 9093 단어 뒤집기
line = int(input())
sentances = [input() for _ in range(line)]
print("\n".join([" ".join([s[::-1] for s in sentance.split()])
                 for sentance in sentances]))
