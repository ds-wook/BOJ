# 10809 알파벳 찾기
string = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = " ".join([str(string.find(s)) for s in alphabet])
print(count)