
a = input("What is your name : ")
b = input("How much do you earn : ")
# If program below takes 1 hr to complete and user has input number instead of name
# Then this is waste of time to run program below so we use " Raise "
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")

print(f"Hello {a}")
# 1000 lines taking 1 hour


c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")

