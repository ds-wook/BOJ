# 4673 셀프넘버
def d(n: int) -> int:
    for i in list(str(n)):
        n = n + int(i)
    return n


set_number = [d(n) for n in range(1, 10000 + 1)]
self_number = [n for n in range(1, 10000 + 1) if n not in set_number]

for s in self_number:
    print(s)
