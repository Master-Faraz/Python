# class Employee:
#     no_of_leaves = 10  # .           Class Variable

#     _protectedVAR=50    #.      Protected Var starts with _
#     __PrivateVAR=100    #.      Private var starts with __

#     def __init__(self, name, salary):  # .                    Constructor
#         self.name = name
#         self.salary = salary

#     def print_details(self):
#         return(f"Name is {self.name} and its salary is {self.salary}")

#     @classmethod
#     # .          Class method is used for changing class instance or variable
#     def change_leaves(cls, new_leaves):
#         cls.no_of_leaves = new_leaves

#     @classmethod
#     def Alternative_Constructor(cls, string):
#         # .  Here *string.split('-') is ARGS splitted by '-'
#         return cls(*string.split('-'))
#         # .          *string.split('-')  ->      Returns list


# F = Employee("Faraz", 1000000)
# A = Employee("Adam", 9999999)


# # print(F.print_details())
# # print(A.print_details())

# # F.no_of_leaves = 80  # .           It will only change for F object not for all
# # print(F.no_of_leaves) #.                  it creates instance variable of F
# # print(A.no_of_leaves)

# # Employee.no_of_leaves=100   #.          it will change class variable
# # print(F.no_of_leaves)

# # .                                  After class method

# # F.change_leaves(50)  # .              It will change class variable
# # print(F.no_of_leaves) #.      OP -> 50
# # print(A.no_of_leaves) #.      OP -> 50


# # Arshad = Employee.Alternative_Constructor("Arshad alam-19919991") #.    Creating Object using Classmethod
# # print(Arshad.print_details())

# # print(F._protectedVAR)  #.          we can print protected var but not private directly
# # print(F.__PrivateVAR)
# # print(F._Employee__PrivateVAR)      #.          for accessing Private var


class A:
    Var = 51  # .                  Class Variable

    def __init__(self):
        self.Var = 191044  # .          Instance Variable

class B(A):
    Var = 99

"""

"""
obj=A
obj2=B




print(obj2.Var)
print(obj.Var)
