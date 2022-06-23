def palindrome(x):                               
    z=x[::-1]                   # HERE WE START WITH LAST CHARACTOR OF "X" AND TAKING STEPS OF "-1"
    if z==x:                      # IN ABOVE IF WE USE  " X[::-1] "   THEN THIS ALSO WORKS
        print(f"{x} is palindrome ")
    else:
        print(f"{x} is not palindrome")
a=input("Enter a name :  ")
palindrome(a)