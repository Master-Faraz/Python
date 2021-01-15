# DEFINE DICTIONARY AND FIND CUBE OF "N" 

def cube(n):
    x={}
    for i in range(1,n+1):          # FROM 1 TO N
        x[i]=i**3
    return print(x)
  
a=int(input("Enter a numer "))
cube(a)