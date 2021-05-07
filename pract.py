n = int(input("Enter size of list you want to create : "))
ls = []

for i in range(n):
    a = int(input(f"Enter {i} th Number : "))
    ls.append(a)

s = set(ls)
ls = list(s)
ls.sort(reverse=True)

print(ls)
