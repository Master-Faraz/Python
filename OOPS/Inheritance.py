class Parent(object):  # .                    Every class inherited from object class
    a = 50
    __b = 60  # .                      Prtected Method

    @classmethod  # .                          Without this our function will not work
    def f_Fun(self):
        print(f"Parent function data type {self.a}")

    def rint():
        print("Normal function in parent class")


class Child(Parent):  # .                      Child inherited from Parent class
    c = 90

    def __init__(self):
        super().__init__()

    @classmethod  # .                          Without this our function will not work
    def P_Fun(self):
        print(f"child function data type {self.c}")

    def rint(self):
        print("Normal function in child class")


obj = Child()

print(obj.c)
print(obj.a)

obj.P_Fun()
obj.rint()

# .                      It returns true if obj is instance of child class
x = isinstance(obj, Child)
print(x)


"""                            *****        Method Overriding       *****
"""


class Parent:

    def __init__(self):
        print("Parent Constructor")
        self.age = 50


class Child(Parent):

    def __init__(self):
        super().__init__()  # .          For not getting erreo
        print("Child constructor ")
        self.weight = 50

# class Grand_Child( Child ): #.                  Multilevel Inheritance
#     pass

# class Multiple( Parent , Child ):   #.              Multilevel inheritance
#     pass


b = Child()

# .         This will give an error as child constructor will override the parent constructor
print(b.age)
print(b.weight)
