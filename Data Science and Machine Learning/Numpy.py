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

y = np.arange(10, 20, 1)  # From 10 to 20 in step of 1
n = np.random.randint(10, 20, 5)  # 5 Random numbers from between 10 to 20


"""
np.zeros((2,5))  -->   Create an array of size (2,5) and initialize it with zeros   ,    dtype -> float64

np.arange(15)  -->   Create an array of size 15 and initialize it with int (0~14)   ,    dtype -> int64

np.linspace(1, 20, 35)  -->   Create an array of size 35 initialize number btw (1~20) in equal space    ,    dtype -> float64

np.empty((4, 6))  -->   Create an 2d-array and initialize it with garbage value   ,    dtype -> float64

np.empty_like(arr)  --> Creates array like array passed and initialize it with garbage values

np.identity(10)   -->  Creates identity matrix of size 10*10   ,   Dtype  -> float64

"""


arr = np.arange(99)
arr = arr.reshape(3, 33)           # It reshapes the 1d-array to form 2d-array
arr = arr.ravel()                # Change back to 1d-array
# print(arr)


"""
Axis in numpy is like dimensions in Matrix         2  3  4
                                                   4  5  6
                                                   7  8  9

axis=0  --> Horizontal Part
axis=1  --> Vertical Part

"""

x = arr_2D.sum(axis=0)      # Sum of column ( Horizontal )
# print(arr_2D)
# print("\n")
# print(x)

x = arr_2D.sum(axis=1)      # Sum of rows ( Vertical )
# print(x)

# print(arr_2D)
# print(arr_2D.T)           # Arr.T    --> Transposes the array
# print(arr_2D.ndim)     #  Returns number of dimensions
# print(arr_2D.nbytes)     #  Returns Total number of Bytes consumed by array


# print(arr.argmax())    #  Returns index of max element  in 1 Dimension Array
# print(arr.argmin())    #  Returns index of min element  in 1 Dimension Array


# print(arr_2D.argmax(axis=0))    # Returns index
# print(arr_2D.argmax(axis=1))    # Returns index

# print(arr_2D.argmax())  #   It converts 2d array to 1d array and then returns index


"""
                            Operations in Array

"""

x = np.arange(10)
y = np.arange(8, 18, 1)  # From 10 to 20 in step of 1


# print(x)
# print(y)
# print()

# print(x+y)      # Addition of array
# print(x*y)      # Multiplication of array
# print(np.sqrt(x))     # Finding Square root

# x = x+5           #         Adding 5 to each element
# x = x*5           #         Multiplying 5 to each element of array

print(np.sin(x))        #       Sin , Cos , tan , log
print(np.sort(x))       #       Sorting an array


print(x.max())
print(x.min())
print(x.sum())



z = np.where(x > 8)  # Returns index of condition
# print(z)


"""

                Some Important Operations on numpy Array

"""


#                   *****       Joining Numpy Arrays        *****


np.vstack((x, y))                   # Creates vertical Stack
np.hstack((x, y))                   # Creates Horizontal Stack
np.column_stack((x, y))             # Creates Stack of columns


#                   *****       Mathematical functions      *****

np.intersect1d(x, y)  # .             Intersection of two arrays
np.setdiff1d(x, y)  # .           Difference of two arrays  -->  x-y

np.sum((x, y), axis=0)  # .                Adding Column Elements
np.sum((x, y), axis=1)  # .                Adding Row Elements

np.mean(x)  # .                Mean of x
np.std(x)  # .                Standard deviation of x
np.median(x)  # .                Median of x
