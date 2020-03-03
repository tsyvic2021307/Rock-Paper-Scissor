from random import randint
import getpass
import rps_modules as rps

names = ["",""]
points = [0,0]
second = None
choices = ["Rock", "Paper", "Scissors"]
currentRound = 1
starter = randint(0, 1)


if starter == 1:
    second = 0
else:
    second = 1

print ("Welcome!")
while len(names[0]) < 2:
    names[0] = input("Player A please enter your first name: ")
while len(names[1]) < 2:
    names[1] = input("Player B please enter your first name: ")

rounds = int(input("How many rounds do you wish to play? "))
print("------------------------------------------\r\n%s has been randomly chosen to start each round of the game." %(names[starter]))


while currentRound < rounds+1:
    startersChoice = rps.weaponChoice(names[starter])[0]
    secondsChoice = rps.weaponChoice(names[second])[0]

    print("------------------------------------------\r\nRound %s Results: %s (%s) vs %s (%s)" %(currentRound, names[0], choices[startersChoice-1], names[1], choices[secondsChoice-1]))

    theResult = rps.checking(startersChoice, secondsChoice)
    if theResult == 0:
        print("This round was a tie!!")
    elif theResult == 1:
        rps.congrats(names[0])
        points[0] += 1
    elif theResult == 2:
        rps.congrats(names[1])
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
    rps.winner(names[0])
elif points[0] < points[1]:
    rps.winner(names[1])
else:
    print("Shouldn't happen")
print("------------------------------------------")