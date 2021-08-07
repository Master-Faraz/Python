# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# d = {
#     'x': [1, 2, 3, 4, 5],
#     'y': [2, 4, 5, 4, 5]
# }

# df= pd.DataFrame(d)

# x = df.iloc[:,0].values.reshape(5,1)
# y = df.iloc[:,1].values


# reg=LinearRegression()
# reg.fit(x,y)

# print(reg.predict([[2.5]]))    #   Predicting from input

# print(reg.predict(x))    #   Predicting values of y_pred from x

# y_pred = reg.predict(x)

# plt.scatter(x,y)    #   Scatter plot of actual x and y
# plt.plot(x,y_pred,color ='r',marker='d')     #   Best fit line of x and Y_pred
# plt.show()

color = "RED"
print(color)

