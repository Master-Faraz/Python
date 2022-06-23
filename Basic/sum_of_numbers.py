total=0
n=int(input("Enter starting number : "))
a=int(input("Enter ending number : "))
for i in range(n,a+1):
    total+=n
    n+=1
print(total)    