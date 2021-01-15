from tkinter import *

root=Tk()                        

# root.geometry("Width x height ")    
root.geometry("455x455")

# weidth , height    --> Syntax for mininum and maximum size

root.minsize(200,200)
root.maxsize(1200,1200)

# Label in tkinter

var=Label(text="This is variable")                 # This Will Show in our GUI
var.pack()                                        # Without this our variable cannot be shown 

root.mainloop()                  
