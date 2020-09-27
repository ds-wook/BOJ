# 다이얼 문제
phone = input()
alpabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
numbers = {a: num + 2 for num, alpha in enumerate(alpabets) for a in alpha}
phone_list = [numbers[p] for p in phone]
phone_time = sum(phone_list) + len(phone_list)
print(phone_time)
`