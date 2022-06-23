# PROGRAM TO PRINT SQUARE OF STRING USING FUNCTION

def fun(n):
    z=[]
    for i in n:
        z.append(i**2)       # FOR ADDING SQUARE VALUES TO 'Z' LIST
    return z
num=list(range(1,11))        # WE USE THIS TO CREATE LIST WHICH CONTAINS NUMBERS FROM 1 TO 10
print(fun(num))
