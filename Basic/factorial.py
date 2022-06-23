def fact(x):
    """ This is doc string"""
    a=1
    while x>=1:
        a=a*x
        x=x-1
    return print(a)
x=int(input("Enter a number "))
fact(x)
print(fact.__doc__)