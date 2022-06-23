# Runner up using list : Means second highest score

n=int(input("Enter length of list : "))
score=[]
for i in range(n):
    a=int(input("Enter a number : "))
    score.append(a)
print('score\n')

z=max(score)
for i in score:
    if i==z:
        score.remove(z)
    else:
        pass
print(f"Runner up is {max(score)}")