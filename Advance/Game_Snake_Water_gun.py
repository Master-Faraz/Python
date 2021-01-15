import random
ls=['s','w','g']
i=0
player=0
computer=0

print('Press s for Snake\n')
print('Press w for Water\n')
print('Press g for Gun\n')

while i<10:
    a=input("Enter your choice : ")
    n=random.choice(ls)    # This will give random from ls

    if (a=='s' and n=='w') or (a=='w' and n=='g') or (a=='g' and n=='s'):
        player =player +1

    elif (n=='s' and a=='w') or (n=='w' and a=='g') or (n=='g' and a=='s'):
        computer =computer +1
    
    else :
        pass
    i+=1

if player > computer:
    print(f'\n**** You win with {player} : {computer} ****\n')
elif player < computer:
    print(f'\n**** You lost with {player} : {computer} ****\n')
else:
    print("**** Game Draw ****")