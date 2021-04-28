# After modification
def comp(a,b):
    l=[]
    for i in a:
        if i in b:
            l.append(i)
    return l         # RETURN MUST BE OUT OF THE LOOP ----> MY MISTAKE
        
       
a=[1,2,3]
b=[1,2,4]
print(comp(a,b))