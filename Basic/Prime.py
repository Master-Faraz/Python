import math as mt

def prime(n):
    if n==1:
        return False
    x=mt.floor(mt.sqrt(n))
    for i in range(2,x+1):
        if(n%i==0):
            return False
    return True



a=int(input("Enter a number : "))
print(prime(a))
