def fibo(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)              # here coma represents seperated by coma
    else:
        print(a,b,end=" ")     # end=" " -----> next print will be seperated by space 
        for i in range(2,n):    # By default it is ( end = "\n" ) 
            c=a+b
            a=b
            b=c
            print(c,end=" ")

a=int(input("Enter how many fibonachhi series you want to print "))
fibo(a)