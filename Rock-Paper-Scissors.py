# Ex 2
# initialising game
from random import randint
import getpass

names = ["",""]
points = [0,0]
second = None
choices = ["Rock", "Paper", "Scissors"]
starter = randint(0, 1)
# set second to alt of starter
print("Sallad waz hea")
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
    print("%s, you've won this round!" %(names[player]))

def winner(player):
    print("Congratulations %s, you won the game!!" %(names[player]))

# get some user inputs / main game
while len(names[0]) < 2:
    names[0] = input("Player A please enter your first name: ")
while len(names[1]) < 2:
    names[1] = input("Player B please enter your first name: ")

rounds = int(input("How many rounds do you wish to play? "))
print("------------------------------------------\r\n%s has been randomly chosen to start each round of the game." %(names[starter]))
currentRound = 1

while currentRound < rounds+1:
    startersChoice = weaponChoice(starter)
    secondsChoice = weaponChoice(second)

    print("------------------------------------------\r\nRound %s Results: %s (%s) vs %s (%s)" %(currentRound, names[0], choices[startersChoice-1], names[1], choices[secondsChoice-1]))

    theResult = checking()
    if theResult == 0:
        print("This round was a tie!!")
    elif theResult == 1:
        congrats(0)
        points[0] += 1
    elif theResult == 2:
        congrats(1)
        points[1] += 1
    elif theResult == 3:
        print("This shouldn't happen...")
    else:
        print("This REALLY shouldn't happen...")
    
    print("------------------------------------------\r\nOverall Points:\r\n%s - %s\r\n%s - %s" %(names[0], points[0], names[1], points[1]))
    
    currentRound += 1
    if currentRound <= rounds:
        getpass.getpass("Press Enter to continue") # if user types anything it won't be visible

print("------------------------------------------")
if points[0] == points[1]:
    print("The game was a tie!")
elif points[0] > points[1]:
    winner(0)
elif points[0] < points[1]:
    winner(1)
else:
    print("Shouldn't happen")
print("------------------------------------------")