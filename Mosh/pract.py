a = {
    "Name": 1,
    "Class": 2,
    "Age": 30
}


# for i in a.values():
#     print(i)

x=map(lambda x: x,a.values())
for i in x:
    print(i)
