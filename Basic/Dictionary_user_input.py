x=dict()
n=int(input("Enter length of dictionary : "));
for i in range(n):
    a=input("Enter a key : ")
    z=int(input("For int value enter 0 else 1 : "))
    if z==0:
        b=int(input("Enter int value : "))
    else:
        b=input("Enter string value : ")
    x.update({a:b})
print(x)