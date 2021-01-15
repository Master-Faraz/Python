import time
import math

def prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n>2 and n%2==0:         # Checking all even is waste of time 
        return False
    max_divisor=math.floor(math.sqrt(n))               # Max divisor is square root of number
    for i in range(3, max_divisor+1 ,2):               # Checking all odd 
        if n%i==0:
            return False
    else:
        return True

count=0
t1=time.time()
for j in range(1,100000):
	if prime(j)==True:
		count+=1
	else:
		count+=0
print(f"Total number of prime number is {count} ")
t2=time.time()
print(f"\t\t\t\tTotal Time taken is {t2-t1} Seconds\n")