# Health management system --> Using functions


import datetime  
def gettime():                              # This function returns date and time  
    return datetime.datetime.now()

def health(a,b,c):
    if a==1 and b==1 and c==1:                    # For Harry this will work 
        m=input("Enter Exercise name :  ") 
        with open('Harry-ex.txt','a') as x:
            x.write(str(gettime())+'\t'+m+'\n')   # Here write function takes only string so we convert gettime to str
            print('\n Data Entered Succesfully -_-\n')
    elif a==1 and b==1 and c==2:
        m=input("Enter food name :  ") 
        with open('Harry-food.txt','a') as x:
            x.write(str(gettime())+'\t'+m+'\n')
            print('\n Data Entered Succesfully -_-\n')

# For Rohan This will work

    elif a==1 and b==2 and c==1:
        m=input("Enter Exercise name :  ") 
        with open('Rohan-ex.txt','a') as x:
            x.write(str(gettime())+'\t'+m+'\n') 
            print('\n Data Entered Succesfully -_-\n') 
    elif a==1 and b==2 and c==2:
        m=input("Enter food name :  ") 
        with open('Rohan-food.txt','a') as x:
            x.write(str(gettime())+'\t'+m+'\n')
            print('\n Data Entered Succesfully -_-\n')

# For Hammad this will work

    elif a==1 and b==3 and c==1:
        m=input("Enter Exercise name :  ") 
        with open('Hammad-ex.txt','a') as x:
            x.write(str(gettime())+'\t'+m+'\n')
            print('\n Data Entered Succesfully -_-\n')  
    elif a==1 and b==3 and c==2:
        m=input("Enter food name :  ") 
        with open('Hammad-food.txt','a') as x:
            x.write(str(gettime())+'\t'+m+'\n')
            print('\n Data Entered Succesfully -_-\n')

# for **** Retriving Data ****

    # Retriving Harry data -->

    elif a==2 and b==1 and c==1:
        with open('Harry-ex.txt') as op:
            for i in op:
                print(i,end='')            
    elif a==2 and b==1 and c==2:
        with open('Harry-food.txt') as op:
            for i in op:
                print(i,end='')


    # Retriving Rohan Data -->

    elif a==2 and b==2 and c==1:
        with open('Rohan-ex.txt') as op:
            for i in op:
                print(i,end='')
    elif a==2 and b==2 and c==2:
        with open('Rohan-food.txt') as op:
            for i in op:
                print(i,end='') 

    # Retriving Hammad Data -->

    elif a==2 and b==3 and c==1:
        with open('Hammad-ex.txt') as op:
            for i in op:
                print(i,end='')
    elif a==2 and b==3 and c==2:
        with open('Hammad-food.txt') as op:
            for i in op:
                print(i,end='')

    else:
        print("\n**** Input Error ****\n PLEASE INPUT AGAIN : ")
        print()
        a=int(input("Press 1 for Log or press 2 for retrive : "))
        b=int(input("Press 1 for Harry , 2 for Rohan , 3 for Hammad : "))
        c=int(input("Press 1 for exercise , 2 for food : "))

# End of function defination -->

a=int(input("Press 1 for Log or press 2 for retrive : "))
b=int(input("\nPress 1 for Harry , 2 for Rohan , 3 for Hammad : "))
c=int(input("\nPress 1 for exercise , 2 for food : "))
print()
health(a,b,c)