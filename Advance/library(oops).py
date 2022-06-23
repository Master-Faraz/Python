class Library:  
    def __init__(self,list_of_books,name):
        self.list_of_books=list_of_books
        self.name=name
        self.issued_books=[]

    def display_books(self):
        return list_of_books
    def lend_books(self):
        x=input("Enter name of book you want to lend : ") 
        if x in list_of_books:   
            if x in self.issued_books:
                q=print("Someone already issued this book -_- ")
                return q
            else:
                self.issued_books.append(x)
                q=print('Book Updated successfully')
                return q
        else:
            w=print('You have entered Wrong book.Please enter again ')
            return w
            
    def add_books(self):
        y=input('Enter name of book : ')
        if y in self.list_of_books:
            e=print('Book is already in list')
            return e
        else:
            list_of_books.append(y)
            e= print('Book updated succesfully ')
            return e
    def return_books(self):
        z=input('Enter name of book you want to return')
        if z in self.issued_books:
            self.issued_books.remove(z)
            r=print('Book returned succesfully')
            return r
        else:
            r=print("You have not issued this book")
            return r


list_of_books=['Harry Potter','Three mens in a boat','Cengage','DC Panday','T']
name=input('Enter your name : ')
obj=Library(list_of_books,name)
print('Press 1 for display books\n Press 2 for lend books \n Press 3 for add books \n Press 4 for return books\n Press 5 to show lended books\n Press 0 for exit\n')
end=False
while end is not True:
    a=int(input("Enter your choice : "))
    if a==0:
        print('***** Bye Bye *****')
        end=True
    elif a==1:
        print(f'{obj.display_books()} \n')
    elif a==2:
        print(obj.lend_books())
    elif a==3:
        print(obj.add_books())
    elif a==4:
        print(obj.return_books())
    elif a==5:
        print(obj.issued_books)
    else:
        print('You have entered wrong option.\n Please enter again')    