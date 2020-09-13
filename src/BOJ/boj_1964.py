# 1964 오각형, 오각형, 오각형....
n = int(input())
five = sum([(4 + 3 * i) if i != 0 else 5 for i in range(n)])
print(five % 45678)