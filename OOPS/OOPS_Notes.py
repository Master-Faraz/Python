class Employee:
    no_of_leaves = 10  # .           Class Variable

    def __init__(self, name, salary):  # .                    Constructor
        self.name = name
        self.salary = salary

    def print_details(self):
        return(f"Name is {self.name} and its salary is {self.salary}")

    @classmethod
    # .          Class method is used for changing class instance or variable
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def Alternative_Constructor(cls, string):
        # .  Here *string.split('-') is ARGS splitted by '-'
        return cls(*string.split('-'))
        # .          cls(*string.split('-'))  ->      Returns list


F = Employee("Faraz", 1000000)
A = Employee("Adam", 9999999)


# print(F.print_details())
# print(A.print_details())

# F.no_of_leaves = 80  # .           It will only change for F object not for all
# print(F.no_of_leaves) #.                  it creates instance variable of F
# print(A.no_of_leaves)

# Employee.no_of_leaves=100   #.          it will change class variable
# print(F.no_of_leaves)

# .                                  After class method

# F.change_leaves(50)  # .              It will change class variable
# print(F.no_of_leaves) #.      OP -> 50
# print(A.no_of_leaves) #.      OP -> 50


Arshad = Employee.Alternative_Constructor("Arshad alam-19919991") #.    Creating Object using Classmethod
print(Arshad.print_details())