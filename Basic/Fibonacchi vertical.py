def fibo(n):
    a=0
    b=1
    if n<=-1:
        print("You are mad")
    elif n==0:
        print("fibonacchi is 0")
    elif n==1:
        print("fibonacchi is 1")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
a=int(input("Enter a number  "))
fibo(a)