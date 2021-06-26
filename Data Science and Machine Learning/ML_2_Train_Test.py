import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("/home/faraz/Documents/Salary_Data.csv")

# x=df["YearsExperience"]
# y=df["Salary"]

x= df.iloc[:,0].values
y= df.iloc[:,1].values

train_x,test_x,train_y,test_y = train_test_split(x,y, test_size = 0.2 , random_state =0)
#   Test size = 0.2 means 20 percent data will be for testing purpose
# print(test_x)
# # print(test_y)
# print(x)
# print(y)

# x.reshape[1,30]
# x=np.array(x)
# # x.reshape(1,30)
# print(x)

train_x=np.array(train_x)
test_x=np.array(test_x)
train_y=np.array(train_y)
test_y=np.array(test_y)
# print(train_x)

reg = LinearRegression()
reg.fit([train_x],train_y)
