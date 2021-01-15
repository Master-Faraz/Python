import numpy as np
from matplotlib import pyplot as pt

x=np.arange(-100,100)
y=x**4 + x**3 +3*(x**2) -9*x

pt.plot(x,y)  
pt.show()