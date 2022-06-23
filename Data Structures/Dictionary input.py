x= dict()
n=int(input("Enter how many values you want to feed in your dictionary \n"))
for i in range(1,n+1):
    key=input("\nEnter a key\n ")
    value=input("\nEnter your value  \n")
    x.update({key:value})
print(x)

