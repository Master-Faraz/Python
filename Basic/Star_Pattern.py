a=int(input("Enter a number : "))
b=int(input("Enter 1 for True 0 for False "))

if b==0:
    i=a
    while a!=0:
        print("*"*a)
        a-=1
elif b==1:
    for i in range(a+1):
        print("*"*i)