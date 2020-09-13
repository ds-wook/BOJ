# 1264 모음의 개수
while True:
    sentence = input().lower()
    count = 0
    if sentence == "#":
        break
    for collection in sentence:
        if collection in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(count)