a=int(input("Enter number of commands : "))
n=[]
for i in range(a):
    x=input("Enter command : ").split(" ")
    b=x[0] 
    if b=="insert":
        n.insert(int(x[1]),int(x[2]))

    if b=="print":
        print(n)

    if b=="remove":
        n.remove(int(x[1]))

    if b=="append":
        n.append(int(x[1]))

    if b=="sort":
        n.sort()

    if b=="reverse":
        n.reverse()

    if b=="pop":
        n.pop()
        
     
