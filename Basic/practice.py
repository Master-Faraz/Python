t = int(input())
ls = []

while(t):
    res = 0
    l = 0
    n, x = input().split(" ")
    n = int(n)
    x = int(x)

    for i in range(n):
        a = int(input())
        if a not in ls:
            ls.append(a)


    res = n-x
    l = len(ls)

    if res <= l:
        print(res)
    else:
        print(l)

    t = t-1
