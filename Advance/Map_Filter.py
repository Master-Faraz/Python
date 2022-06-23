ls=[1,2,3,4,5,6,7,8,9]

m=list(map((lambda x:x*x),ls))
print(m)

f=list(filter((lambda x: x*x>25),ls))
print(f)