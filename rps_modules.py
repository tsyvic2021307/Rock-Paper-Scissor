import getpass

# game methods
def weaponChoice(player):
    theString = "------------------------------------------\r\n%s, please choose your weapon:\r\n1. Rock\r\n2. Paper\r\n3. Scissors\r\nEnter your choice (use the appropriate number): " %(player)
    choice = int(getpass.getpass(theString))
    return choice, theString

def checking(starter, second): # check the result of choices
    diff = starter - second
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
    print("%s, you've won this round!" %(player))

def winner(player):
    print("Congratulations %s, you won the game!!" %(player))