# 1157 단어 공부
string = input().upper()
dic = {alphabet : 0 for alphabet in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

for alphabet in string:
    if alphabet in dic:
        dic[alphabet] += 1
        
list_alphabet = [alphabet for alphabet in string if dic[alphabet] == max(dic.values())]
output = "?" if len(set(list_alphabet)) > 1 else list_alphabet[0]
print(output)