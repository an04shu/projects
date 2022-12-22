import random
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='p'
elif random:
    comp='sc'
def gamecheck(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='sc':
            return  False
    elif comp=='p':
        if you=='s':
            return False
        elif you=='sc':
            return True
    elif comp=='sc':
        if you=='s':
            return True
        elif you=='p':
            return False
you=input("Choose s(stone),p(paper) or sc(scissor)\n")
print("Loading.......Comp turn")
print(f'You choosed {you}\n')
print(f'Comp choosed {comp}\n')
a=gamecheck(comp,you)
if a==None:
    print("The game is a tie")
elif a:  
    print('You win')
else:
    print('You lose')