import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], np.int64)


# print(arr[0])
# print(arr.dtype)

"""
np.int64 is dtype of our array  -->  By Default it is int32
np.int64 is optional

"""
arr_2D = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])  # 2D Array

# print(arr_2D.shape)     #    Shape will return Dimension of array
# print(arr_2D.dtype)
# print(arr_2D.dtype)


arr_zero = np.zeros((2, 5))
# print(arr_zero.shape)  #  2,5
# print(arr_zero.dtype)  # float64
# print(arr_zero.size)   # 10

arr_range = np.arange(15)
# print(arr_range)  # 0~14
# print(arr_range.dtype)   # Int 64

arr_line = np.linspace(1, 20, 35)
# print(arr_line)
# print(arr_line.dtype)   # Float64
# print(arr_line.size)   # 35

arr_empty = np.empty((4, 6))
# print(arr_empty)
# print(arr_empty.dtype)

arr_like = np.empty_like(arr)
# print(arr_like)
# print(arr_like.dtype)

arr_Identity_matrix = np.identity(10)
# print(arr_Identity_matrix)
# print(arr_Identity_matrix.dtype)


"""
np.zeros((2,5))  -->   Create an array of size (2,5) and initialize it with zeros   ,    dtype -> float64

np.arange(15)  -->   Create an array of size 15 and initialize it with int (0~14)   ,    dtype -> int64

np.linspace(1, 20, 35)  -->   Create an array of size 35 initialize number btw (1~20) in equal space    ,    dtype -> float64

np.empty((4, 6))  -->   Create an 2d-array and initialize it with garbage value   ,    dtype -> float64

np.empty_like(arr)  --> Creates array like array passed and initialize it with garbage values

np.identity(10)   -->  Creates identity matrix of size 10*10   ,   Dtype  -> float64

"""


arr=np.arange(99)
arr=arr.reshape(3,33)   #   It reshapes the 1d-array to form 2d-array
arr=arr.ravel()
print(arr)
