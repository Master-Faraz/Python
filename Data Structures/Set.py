first_set = {1, 2, 3, 4, 5}

num = [3, 4, 5, 6, 7, 8]

second_set = set(num)

# print(type(num))
# print(type(first_set))

'''

Set is a DS of UNIQUE and unordered pair of numbers
Set doesnot support indexing ex :->    We cannot use  first_Set[1]

'''
#                   *****       Operations      *****

first_set.add(6)
first_set.remove(6)

"""
Union we use (a | b)
Intersection we use (a & b)
Difference we use (a - b)
Symmetric Difference (a ^ b)

"""

print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)
print(first_set ^ second_set)
