def fun(name, *data):  # .                  Here *data -->  *args   ->  Argument
    print(name)
    for i in data:
        print(i)


fun("Faraz", 191044, "CSE", "NSIT", 8210189562)


def fun(name, **data):  # .                  Here **data -->  *kwargs  ->  Keyword Argument
    print(name)
    for i in data.values():
        print(i)


fun("Faraz", roll=191044, branch="CSE", clg="NSIT", no=8210189562)


"""

def function_name_print(a, b, c, d, e): 

    print(a, b, c, d, e, f )    --> # If we add f , This will show error so 

                                    # we introduce *args and **kwargs so that we can add various elements 

                                    # *args for tuple or list and **kwargs for dictionary 

 

 

# We can write *args and **Kwargs as any name srarts with * and ** respectively  

 

 

def funargs(normal, *args, **kwargs): 

    print(normal) 

    for item in args: 

        print(item) 

    print("\nNow I would Like to introduce some of our heroes") 

    for key, value in kwargs.items(): 

        print(f"{key} is a {value}") 

 

# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam") 

 

 

har = ["Harry", "Rohan", "Skillf", "Hammad","Shivam", "The programmer"]        # This is args                   

normal = "I am a normal Argument and the students are:" 

kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor","The Programmer": "Coordinator", "Shivam":"Cook"}   # This is kwargs 

 

funargs(normal, *har, **kw)   # for calling we must use * for args and ** for kwargs 

"""
