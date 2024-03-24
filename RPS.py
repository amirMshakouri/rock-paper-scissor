import random as rn 

mosht_yek = ["sang","kaghaz","gheichi"]
mosht_do = ["sang","kaghaz","gheichi"]

print()
print()
print()

print("******welcome to rock, paper cissors game (FIRST EDITION)******")

print()
print()
print()

answer=""

def keep_going():

    answer = input("Do you wish to continue?")

    if answer == "yes":
        print("You have chosen to continue on")
    else:
        print("You have chosen to quit this program")
        quit()

print("for starting the game write (yes) ")    
print("for exitting the game write (no)")

keep_going()


player_aval=input("who is player one ?" )
player_dovom=input("who is player two ?" )

dast_yek=""
dast_do=""


def shuffle_mosht():
    for i in range(3):
        rn.shuffle(mosht_yek)
        rn.shuffle(mosht_do)
    
    dast_yek =rn.choice(mosht_yek)
    print(f"{player_aval}'s choice is: {dast_yek}")
    
    dast_do =rn.choice(mosht_do)
    print(f"{player_dovom}'s choice is: {dast_do}")
    return (dast_yek , dast_do)

shuffle_mosht()

def game():
    if dast_yek == dast_do =="sang":
        print("draw")
    elif dast_yek and dast_do == "kaghaz":
        print("draw")
    elif dast_yek and dast_do == "gheichi":
        print("draw")
    elif dast_yek == "kaghaz" and dast_do == "sang":
        print(f'winner is {player_aval}')
    elif dast_yek == "gheichi" and dast_do == "kaghaz":
        print(f'winner is {player_aval}')
    elif dast_yek == "sang" and dast_do == "gheichi":
        print(f'winner is {player_aval}')
    else:
        print(f'winner is {player_dovom}')

game()

print(__name__)