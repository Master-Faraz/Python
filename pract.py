class Employee:
    no_of_leaves = 10

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        

    def print_details(self):
        return(f"Name is {self.name} and its salary is {self.salary}")


F=Employee("Faraz",1000000)
A=Employee("Adam",9999999)

print(F.print_details())
print(A.print_details())