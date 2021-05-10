class container:

    def __init__(self):
        self.Dictionary = {}

    def add(self, i):
        self.Dictionary[i] = self.Dictionary.get(i, 0) + 1

        # self.var.get(i, 0) + 1    ->   here we check If i in dictionary then increment i with 1
        # If not then we supply 0 to it

    """             Some Magic Methods
    """

    def __getitem__(self, key):  # .         for getting the key
        # .                  here are getting value of given key
        return self.Dictionary.get(key, 0)

    def __setitem__(self, key, value):
        self.Dictionary[key] = value

    def __len__(self):
        return len(self.Dictionary)

    def __iter__(self):
        return iter(self.Dictionary)    #.                  iter is built in function


obj = container()

obj.add("Hello")
obj.add("Hello")
obj.add("Hello")
obj.add("hello")
# # print(obj.Dictionary)

# print(obj["Hello"])  # .    using  __getitem__

# obj["Hello"] = 5  # .    using  __setitem__

# print(obj["Hello"])

# print(obj.__len__())    #.                      It is used to print the length using  __len__


for i in obj.__iter__():
    print(i)

