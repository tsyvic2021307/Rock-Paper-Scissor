# Ex 1
# initialising game
from random import randint
import getpass

names = ["",""]
starter = randint(0, 1)
second = None
choices = ["Rock", "Paper", "Scissors"]
# set second to alt of starter
if starter == 1:
    second = 0
else:
    second = 1

# game methods
def weaponChoice(player):
    choice = int(getpass.getpass("------------------------------------------\r\n%s please choose your weapon:\r\n1. Rock\r\n2. Paper\r\n3. Scissors\r\nEnter your choice (use the appropriate number): " %(names[player])))
    return choice

def checking(): # check the result of choices
    diff = startersChoice - secondsChoice
    if diff == 0:
        result = 0 # tie
    elif diff == 1 or diff == -2:
        result = 1 # starter win
    elif diff == -1 or diff == 2:
        result = 2 # second win
    else:
        result = 3 # err
    return result

def congrats(player):
    print("Congrats %s, you've won the match!" %(names[player]))


# get some user inputs / main game
while len(names[0]) < 2:
    names[0] = input("Player A please enter your first name: ")
while len(names[1]) < 2:
    names[1] = input("Player B please enter your first name: ")

print("------------------------------------------\r\n%s has been randomly chosen to start the game." %(names[starter]))

startersChoice = weaponChoice(starter)
secondsChoice = weaponChoice(second)

print("------------------------------------------\r\nResults: %s (%s) vs %s (%s)" %(names[0], choices[startersChoice-1], names[1], choices[secondsChoice-1]))

theResult = checking()
if theResult == 0:
    print("The game was a tie!!")
elif theResult == 1:
    congrats(0)
elif theResult == 2:
    congrats(1)
elif theResult == 3:
    print("This shouldn't happen...")
else:
    print("This REALLY shouldn't happen...")