#                       *****   Filter Function *****

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = list(filter(lambda i: i % 2 == 0, a))
print(x)  # Filter is used to filter something

#                       *****   Map Function    *****

d = {
    "Name": "Faraz",
    "clg": "NSIT",
    "Roll": 191044,
    "Reg": 19105103033
}
y = list(map(lambda i: i, d.values()))
print(y)  # Map is used to get certain values


"""

Map and filter returns iterable object that canbe coverted into list directly

"""

z = [i for i in a if i % 3 == 0]
print(z)  # List comprehension


#                       *****       Zip Function        *****


ZIP = list(zip("abc", x, y, z))
print(ZIP)

"""

Zip function is used to convert two or more iterable object and convert it into a single
zip object which contains equal pair of tupples

"""
