# PROGRAM TO PRINT REVERSE OF LIST

# FIRST METHOD ------>

def rev(l):
    l.reverse()
    return l
a=[1,2,3,4]
print(rev(a))

# SECOND METHOD ----->

def reverse(l):
    return l[::-1]
a=[5,6,7,8]
print(reverse(a))

# THIRD METHOD ------->

def reve(l):
    x=[]
    for i in range(len(l)):
        y=l.pop()
        x.append(y)
    return x

a=[9,10,11,12]
print(reve(a))

