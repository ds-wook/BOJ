# 1546 평균
N = int(input())
scores = [int(score) for score in input().split()][:N]
new_score = [score / max(scores) * 100 for score in scores]
new_avg = sum(new_score) / len(new_score)
print(new_avg)