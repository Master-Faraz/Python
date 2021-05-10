class container:

    # def __new__(self):  # .                  it always called before __init__  constructor
        # .                  Here init has only one parameter so we give only one parameter to __new__
        # print("The object is getting initialized")

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
        # .                  iter is built in function returns iterator object
        return iter(self.Dictionary)


obj = container()

obj.add("Hello")
obj.add("Hello")
obj.add("Hello")
obj.add("hello")
# print(obj.Dictionary)

print(obj["Hello"])  # .    using  __getitem__

obj["Hello"] = 5  # .    using  __setitem__

print(obj["Hello"])

print(obj.__len__())    #.                      It is used to print the length using  __len__


for i in obj.__iter__():    #.                  using __iter__
    print(i)
