# Program to print second lowest marks student got

if __name__ == '__main__':
    record=[]
    marks=[]
    n=int(input())
    for i in range(n):
        name = input()
        score = float(input())
        z=[name,score]
        record.append(z)
        marks.append(score)
    a=(sorted(set(marks)))[1]                     # Here we convert list to set to remove repetition 
    for i,j in sorted(record):                    # And use sorted function to sort and convert into list
        if j==a:
            print(i)
