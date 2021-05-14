from typing import NewType


l = []
for i in range(0, 3):
    tic = input()
    l.append(tic)

cx = 0
co = 0
n = 0
# print(l)
for i in l:
    for j in i:
        if(j == 'X'):
            cx += 1
        elif(j == 'O'):
            co += 1
        elif(j == '_'):
            n += 1
print(cx)
print(co)
print(n)