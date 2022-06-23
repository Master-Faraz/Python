A = [("Product 1", 250), ("Product 2", 150), ("Product 3", 350)]

# For sorting we use

A.sort(key=lambda A: A[1], reverse=True)  # Sort in reverse order
print(A)


#                       *****       Map Function      *****

# map function executes command to every item in iterable

price = list(map(lambda A: A[1], A))
print(price)
price = [item[1] for item in A]  # Using list comprehension
print(price)


#                       *****       filter Function      *****

# filter function checks the condition and returns iterables

price = list(filter(lambda A: A[1] >= 200, A))
print(price)

price = [item for item in A if item[1] >= 200]  # Using list comprehension
print(price)


#                    *****         Zip function          *****
a=[1,2,3,4]
b=[10,20,30,40]
print(list(zip(a,b)))