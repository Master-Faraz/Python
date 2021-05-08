def fun(a,b):
    return a+b

@fun
def mod_fun(func):

    def another(*args,**kwargs):
        print("Started")
        v=func(*args,**kwargs)
        print("End")
        return v

    return another
    

print(mod_fun(5,6))