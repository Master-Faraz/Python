def check(n):
    x=[]
    y=[]
    for i in n:
        if i%2==0:
            x.append(i)
        else:
            y.append(i)
    op=[x,y]
    return op               
    
a=list(range(0,8))    
print(check(a))