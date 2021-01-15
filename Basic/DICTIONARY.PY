# DICTIONARY INFO

x={"name":"faraz","age":19,'year':2020}
y={'Name':"ali", "Age":20,"dob":1999}

# LOOPS IN DICTIONARY ------->

for i in x:
    print(i)                                 # IT PRINTS ONLY KEY
print("\n\n")

for i in x.values():                         #IT PRINTS ONLY VALUES
    print(i)
print("\n\n")


# REMOVE SOMETHING FROM DICTIONARIES -------------------->

x.pop("name")
print(x)                                        # IT REMOVES ONLY SPECIFIED KEY

print("\n\n")

x.popitem()                                     # IT REMOVES SOMETHING FROM DICTIONARY AT RANDOM
print(x)


# UPDATE METHOD ------------------------------------------>

x.update(y)
print(x)                                         # UPDATE TWO DICTIONARY OR ADDING SOMETHING TO ONE DICTIONARY   
