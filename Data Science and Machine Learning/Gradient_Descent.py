import numpy as np
import time

def grad(x,y):
    m_curr = b_curr =0       # Start with some value of M and B
    iterations = 2000       # Iterations to reach minima
    n = len(x)               # Length of array or dataset
    learning_rate = 0.06    # Steps to reach minima 
    
    minimum = (1/n) * sum([val**2 for val in (y-(m_curr * x +b_curr))])     # Minimum = Error
    
    for i in range(iterations):  
        m_prev=m_curr
        b_prev=b_curr

        y_pred = m_curr * x +b_curr     #  Y = MX + C
        md = -(2/n)*sum(x*(y-y_pred))   # M partial derivative
        bd = -(2/n)*sum((y-y_pred))   # B partial derivative
        error = (1/n) * sum([val**2 for val in (y-y_pred)])   #   Or cost function



        if(error>minimum):
            print(f"Slope M : {m_prev} and Intercept B : {b_prev} ")
            break
        if(error<minimum):            
            minimum=error

        

        m_curr = m_curr -learning_rate * md
        b_curr = b_curr -learning_rate * bd
        
        # print(f"Error : {error} \t m : {m_curr} \t b : {b_curr} \t Iterations {i}")
        # We keep on reducing error ::  by increasing iterationsns 
 
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])


t1=time.time()

grad(x,y)

t2 = time.time()

print(f"\n\nTime taken is : {t2-t1}\n\n")
    
    
"""
1 > We check by decreasing or increasing Learning Rate
2 > when error starts increasing that will be our upper_boundry  ex at learning rate 0.1 , iteration 100
3 > When boundry is found then we decrease the learning rate and increasing iterations to get optimal value where error is minimum
4 > at 0.06 and 2000  we get M_curr ~=2 , B_curr ~= 3 
5 > Y = 2x + 3    is the equation

"""