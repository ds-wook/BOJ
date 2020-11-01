string = input()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in cro_alpha:
    string = string.replace(c, '0')
print(len(string))
