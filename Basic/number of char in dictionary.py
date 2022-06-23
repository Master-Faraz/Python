#COUNT NUMBER OF CHAR IN DICTIONARY

def x(n):
    count={}
    for i in n:
        count[i]=n.count(i)
    return print(count)

n="faraz ali ahmad"
x(n)