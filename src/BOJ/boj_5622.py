# 다이얼 문제
import sys
from typing import Dict


def phone_time(numbers: Dict[str, int]) -> int:
    phone_list = [numbers[p] for p in phone]
    return sum(phone_list) + len(phone_list)


phone = sys.stdin.readline().strip()
alpabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
numbers = {a: num + 2 for num, alpha in enumerate(alpabets) for a in alpha}

print(phone_time(numbers))
