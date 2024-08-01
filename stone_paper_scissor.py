#Stone paper sicssor
import random

'''
1 for stone 
-1 for paper
0 for scissors
''' 
computer=random.choice([-1,0,1])
youstr=input("Enter Your Choice : ")
youdict={"stone":1,"paper":-1,"scissor":0}
reversedict={1:"stone",0:"scissor",-1:"paper"}
you=youdict[youstr]
print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if computer==you:
    print("Draw !")
else:
    if computer==-1 and you==1:
        print("You Lose !")
    elif computer==-1 and you==0:
        print("You Win !")
    elif computer==-1 and you==-1:
        print("Draw !")
    if computer==1 and you==-1:
        print("You Win !")
    elif computer==1 and you==0:
        print("You Lose !")
    elif computer==1 and you==1:
        print("Draw !")
    if computer==0 and you==1:
        print("You Win !")
    elif computer==0 and you==-1:
        print("You Lose !")
    elif computer==0 and you==0:
        print("Draw !")
