class Product:

    def __init__(self, price):  # .          constructor for setting price
        self.price = price

    @property  # .                      Using Property method decorator we can use datatype as property  -->   obj.price
    def price(self):
        return self.__price  # .            __ means private member

    @price.setter  # .                      For setting the price
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


b = Product(5)
print(b.price)

c = Product(-5)  # .                  Will give exception
print(c.price)
