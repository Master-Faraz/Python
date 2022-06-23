# fibonacchi using recurssive approach
# logic is fibo of n is sum of fibo of n-1 and n-2

def fibo(n):
    if n<=0:
        return('Enter a Natural number')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
a=int(input("Enter a number : "))
print(fibo(a))