def gen(n):                     # Factorial using Generators
    total=1
    for i in range(n):
        total*=n
        n-=1
    yield total

a=int(input("Enter a number : "))
fibo=gen(a)
for i in range(a):
    print(fibo.__next__())

