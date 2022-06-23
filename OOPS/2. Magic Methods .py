class Rectangle:

    def __init__(self, length, bredth):  # .                  Constructor
        self.length = length
        self.bredth = bredth

    def func(self):
        print(f"{self.length} : {self.bredth}")

    def area(self):
        return self.length*self.bredth

    @classmethod
    def zero(cls):
        # .                  Just like writting ->   A = Rectangle(0,0)
        return cls(0, 0)

    """                 *****       Magic Methods       *****

    Just like Operator Overloading

    """

    def __str__(self):  # .                      Converts to string
        return f"{self.length} : {self.bredth}"

    def __eq__(self, other):  # .                      Equal to
        return self.length == other.length and self.bredth == other.bredth

    def __gt__(self, other):  # .                      Greater than
        return self.length > other.length and self.bredth > other.bredth
    


    

if __name__=='__main':

    A = Rectangle(5, 6)
    # A.func()
    # print(A.area())

    B = Rectangle.zero()  # .                  Class_Method -> it initializes with zeros
    # B.func()

    """
                        *****       Without Magic Method these methods are not workable     *****

        Print( Object ) 
        print( object_1 > object_2)
        print( object_1 = object_2)
        print( object_1 < object_2)

    """
    # print(A)
    # print(A == B)
    # print(A > B)
    # print(A != B)

