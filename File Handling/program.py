import datetime


def fun():
    return datetime.datetime.now()


choice = int(input("Press 1 for Enter Data or Press 2 For Retriving data : "))

if choice == 1:  # .                      For Setting Data

    name = input("Enter your name : ")
    data = int(input("Enter 1 for EXERCISE  or Enter 2 for Diet "))

    n = name.upper()

    if n == "FARAZ":
        if data == 1:
            with open('Faraz_Exercise.txt', 'a') as f:
                command = input("Enter your Exercise name : ")
                f.write(str(fun())+"\t"+command+"\n")
                print("\t\t***  Written Successfully  ***\t\t")

        elif data == 2:
            with open("Faraz_Diet.txt", "a") as f:
                command = input("Enter your food name : ")
                f.write(str(fun())+"\t"+command+"\n")
                print("\t\t***  Written Successfully  ***\t\t")

    if n == "ADAM":
        if data == 1:
            with open("Adam_Exercise.txt", "a") as f:
                command = input("Enter your Exercise name : ")
                f.write(str(fun())+"\t"+command+"\n")
                print("\t\t***  Written Successfully  ***\t\t")

        elif data == 2:
            with open("Adam_Diet.txt", "a") as f:
                command = input("Enter your food name : ")
                f.write(str(fun())+"\t"+command+"\n")
                print("\t\t***  Written Successfully  ***\t\t")


if choice == 2:  # .                      For Getting Data

    name = input("Enter your name : ")
    data = int(input("Enter 1 for EXERCISE  or Enter 2 for Diet "))
    n = name.upper()

    if n == "FARAZ":
        if data == 1:
            with open("Faraz_Exercise.txt", "rt") as f:
                print(f.readlines())

        elif data == 2:
            with open("Faraz_Diet.txt", "rt") as f:
                print(f.readlines())

    if n == "ADAM":
        if data == 1:
            with open("Adam_Exercise.txt", "rt") as f:
                print(f.readlines())

        elif data == 2:
            with open("Adam_Diet.txt", "rt") as f:
                print(f.readlines())
