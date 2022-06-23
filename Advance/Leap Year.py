# 1992 and 2100
def is_leap(year):
    leap = False
    
    if year%400==0 or ( year%100!=0  and year%4==0):
        return True
    else:
        return False
    

year = int(input("Enter year  "))
print(is_leap(year))


# n the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.