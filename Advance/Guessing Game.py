import random
y=random.randint(0,10)
x=int(input("Enter a number "))
guess=1
end=False
while not end :                                           # Jabtak true nahi ho jata Tab-tak loop chalega.
    if x== y:
        print(f"you won in {guess} attempt")
        end=True
    else:
        if x <= y:
            print("too low ")
            guess+=1
            x=int(input("Enter number again "))
        else:
            print("too high ")
            guess+=1
            x=int(input("Enter number again "))

# We can also use in else ststement using DRY CODING------
# else:
#       if x <= y:
#           print("too low ")
#       
#       else:
#           print("too high ")
#       guess+=1
#       x=int(input("Enter number again ")) # OUTSIDE IF ELSE STATEMENT_-_

