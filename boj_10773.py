import sys
# 시간 줄이고 싶을 시 입력 함수 불러오기
line = int(sys.stdin.readline())
number = []
for _ in range(line):
    num = int(sys.stdin.readline())
    if num == 0:
        number.pop()
    else:
        number.append(num)
print(sum(number))