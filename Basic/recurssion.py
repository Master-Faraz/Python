def comp(a,b):
    if a>b:
        return a
    else:
        return b
                    # RECURSSION-- FUNCTION CALLING ITSELF
def new(a,b,c):
    z=comp(a,b)
    return comp(z,c)       # WE CAN ALSO USE " return comp(comp(a,b),c)" AND ELIMINATE STEP 8
a=int(input("Enter first number  "))
b=int(input("Enter second number  "))
c=int(input("Enter third number  "))
print(new(a,b,c))