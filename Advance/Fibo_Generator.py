def fibo(n):
    a = 0
    b = 1

    if(n == 1):
        yield(a)

    elif(n == 2):
        yield(b)

    else:
        yield(a)
        yield(b)
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            yield(c)


a = int(input("Enter how many fibo you want to get : "))
x=fibo(a)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
