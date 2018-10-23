import time, sys, os, termcolor, pygame
from termcolor import colored

pygame.init()
hit = pygame.mixer.Sound("zoop.wav")
win = pygame.mixer.Sound("clapping.wav")
ship = pygame.mixer.Sound("duck.wav")
miss = pygame.mixer.Sound("goose.wav")
ship_exists = pygame.mixer.Sound("water_drop.wav")
wrong_char = pygame.mixer.Sound("snap.wav")

letters = ["A", "B", "C", "D", "E", "F", "G"]  # for validation
digits = [1, 2, 3, 4, 5, 6, 7]  # for validation
dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
tab1 = []  # player's A letter ship coordinates (see def: ship_location)
tab2 = []  # player's A digit ship coordinates (see def: ship_location)
tab3 = []  # player's B letter ship coordinates (see def: ship_location)
tab4 = []  # player's B digit ship coordinates (see def: ship_location)

# EMPTY BOARDS (At the beginning the tables are empty)
#       0       1     2     3     4     5     6     7     8     9     10    11    12    13    14
A = ["║ A ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
B = ["║ B ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
C = ["║ C ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
D = ["║ D ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
E = ["║ E ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
F = ["║ F ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
G = ["║ G ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ "]
Z = [A,B,C,D,E,F,G]

Z1 = [[column for column in row] for row in Z]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FOR CLEANING BOTH BOARDS
def cleaning_data_in_board():
    for x in range(7):
        for i in range(0,14,2):        
            Z[x][i+1] = " "
            Z1[x][i+1] = " "

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FOR REFRESHING PLAYER'S A BOARD -> FOR BOTH PLAYERS (a=1 -> PLAYER A)(a=2 -> PLAYER B)
def drawing_board_edges_with_data(a):
    if(a == 1):
        print(colored("╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗", "yellow"))
        print(colored("║   ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║ 6 ║ 7 ║", "yellow"))
        print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣", "yellow"))

        for i in Z:
            x = ""
            for let in i:
                x += "" + let
            if(i != G):
                print(colored(x, "yellow"))
                print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣", "yellow"))
            elif(i == G):
                print(colored(x, "yellow"))
                print(colored("╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝", "yellow"))

    elif(a == 2):
        print(colored("╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗", "green"))
        print(colored("║   ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║ 6 ║ 7 ║", "green"))
        print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣", "green"))

        for i in Z1:
            x = ""
            for let in i:
                x += "" + let
            if(i != Z1[6]):
                print(colored(x, "green"))
                print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣", "green"))
            elif(i == Z1[6]):
                print(colored(x, "green"))
                print(colored("╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝", "green"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ADDING & TO THE BOARD -> FOR BOTH PLAYERS (z=1 -> PLAYER A)(z=2 -> PLAYER B)
def data_swap(x, y, z):
    if(z == 1):
        for litera in letters:
            if litera == x:
                Z[dictionary[litera]][y] = "&"
        drawing_board_edges_with_data(1)  # refresh Player's A board

    elif(z == 2):
        for litera in letters:
            if litera == x:
                Z1[dictionary[litera]][y] = "&"
        drawing_board_edges_with_data(2)  # refresh Player's B board

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# VALIDATION
def if_not_in_letters(x):
    if(x not in letters):
        wrong_char.play()
        print(colored("Wrong char!", "red"))
        time.sleep(0.7)
        return False
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# VALIDATION
def if_not_in_digits(y):
    try:
        y = int(y)
    except ValueError:  # ValueError appears when user inputs not digits
        print(colored("Wrong char!", "red"))
        return False
    if(y not in digits):
        wrong_char.play()
        print(colored("Wrong char!", "red"))
        time.sleep(0.7)
        return False
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHANGING SMALL LETTERS FOR BIG LETTERS IN USER INPUTS
def toUppercase(lit):
    if lit.isupper():
        return lit
    else:
        return lit.upper()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHECKING SHIP EXISTING -> FOR BOTH PLAYERS
def isShipExists(a, lit, number):
    if(a == 1):
        for x in tab1:
            if x == lit:
                posX = tab1.index(lit)
                if tab2[posX] == number:
                    print(colored("Ship exists already!!!", "red"))
                    return True
        return False

    if(a == 2):
        for x in tab3:
            if x == lit:
                posX = tab3.index(lit)
                if tab4[posX] == number:
                    print(colored("Ship exists already!!!", "red"))
                    return True
        return False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SHIP LOCATION -> FOR BOTH PLAYERS
def ship_location(a):

    k = 4  # because our ships are fourfold, threefold and double
    s = 1
    while(s <= 3):  # because there are 3 ships
        z = 1  # because we start from the first *

        while(z <= k):
            if(a == 1):
                print(colored("PLAYER A", "yellow") +
                      " - put the ships in the board")
            elif(a == 2):
                print(colored("PLAYER B", "green") +
                      " - put the ships in the board")
            print(f"Ship {k}-mast:")
            while True:
                lit = toUppercase(input(f"Press {z} letter coordinate: "))
                if if_not_in_letters(lit):  # validation
                    break

            while True:
                number = input(f"Press {z} digit coordinate: ")
                if if_not_in_digits(number):  # validation
                    number = int(number)
                    break

            if isShipExists(a, lit, number):
                continue

            if(a == 1):
                tab1.append(lit)                
            elif(a == 2):
                tab3.append(lit)                
            if(a == 1):
                tab2.append(number)                
            elif(a == 2):
                tab4.append(number)

            # we need to translate the user choice, because our board has different coordinates (look at the top)
            number = 2*number-1
            os.system("clear")

            data_swap(lit, number, a)
            ship.play()
            time.sleep(0.3)
            z += 1
        s += 1
        k -= 1
    time.sleep(1.5)
    os.system("clear")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# GIVE X (IF HIT) -> FOR BOTH PLAYERS (C=1 -> PLAYER A)(C=2 -> PLAYER B)
def give_X(a, b, c):

    if(c == 1):
        for litera in letters:
            if litera == a:
                Z[dictionary[litera]][b] = "X"
        drawing_board_edges_with_data(1)  # refresh Player's A board

    elif(c == 2):
        for litera in letters:
            if litera == a:
                Z1[dictionary[litera]][b] = "X"
        drawing_board_edges_with_data(2)  # refresh Player's B board

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# GIVE O (if miss)-> FOR BOTH PLAYERS
def give_O(a, b, c):

    if(c == 1):
        for litera in letters:
            if litera == a:
                Z[dictionary[litera]][b] = "0"
        drawing_board_edges_with_data(1)

    elif(c == 2):
        for litera in letters:
            if litera == a:
                Z1[dictionary[litera]][b] = "0"
        drawing_board_edges_with_data(2)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# RULES FOR SHOOTING
def rules():
    print(colored("╔═══╗", "magenta"))
    print(colored("║   ║  -> You may shoot here", "magenta"))
    print(colored("╚═══╝", "magenta"))
    print(colored("╔═══╗", "magenta"))
    print(colored("║ X ║  -> You hit here", "magenta"))
    print(colored("╚═══╝", "magenta"))
    print(colored("╔═══╗", "magenta"))
    print(colored("║ O ║  -> You missed here", "magenta"))
    print(colored("╚═══╝", "magenta"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SHOOTING -> FOR BOTH PLAYERS
def shooting():
    starsA = 9  # for win condition
    starsB = 9  # for win condition
    player = "A"  # Player A starts shooting
    while(True):
        if(player == "A"):
            os.system("clear")
            drawing_board_edges_with_data(1)
            rules()
            print("SHOOTING! " + colored("Player A", "yellow") + " is shooting")
            bang1 = toUppercase(input("Letter coordinate: "))
            if not if_not_in_letters(bang1):
                continue
            bang2 = input("Digit coordinate: ")
            if  not if_not_in_digits(bang2):                
                continue
            bang2 = int(bang2)
            if((bang1 in tab3) and (bang2 in tab4)):  # PLAYER A HIT
                hit.play()
                print(colored("Hit! Try again!", "green"))
                time.sleep(1.5)
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_X(bang1, bang2, 1)  # if hit -> give X
                starsA -= 1
                if(starsA == 0):  # win condition
                    print("WTF?! " + colored("Player A", "yellow") + " wins!")
                    win.play()
                    time.sleep(3)
                    sys.exit(0)

            else:  # miss
                miss.play()
                time.sleep(0.4)
                print(colored("MISS! " + colored("Player B",
                                                 "green") + " starts shooting", "red"))
                time.sleep(2)
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_O(bang1, bang2, 1)  # if miss -> give O
                player = "B"

        elif(player == "B"):
            os.system("clear")
            drawing_board_edges_with_data(2)
            rules()
            print("SHOOTING! " + colored("Player B", "green") + " is shooting")
            bang1 = toUppercase(input("Letter coordinate: "))
            if not if_not_in_letters(bang1):
                continue
            bang2 = input("Digit coordinate: ")
            if not if_not_in_digits(bang2):
                continue
            bang2 = int(bang2)
            if((bang1 in tab1) and (bang2 in tab2)):  # PLAYER B HIT
                hit.play()
                print(colored("Hit! Try again!", "green"))
                time.sleep(1.5)
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_X(bang1, bang2, 2)  # if hit -> give X
                starsB -= 1
                if(starsB == 0):  # win condition
                    print("WTF?! " + colored("Player B", "green") + " wins!")
                    win.play()
                    time.sleep(3)
                    sys.exit(0)

            else:  # miss
                miss.play()
                time.sleep(0.4)
                print(colored("MISS! " + colored("Player A",
                                                 "yellow") + " starts shooting", "red"))
                time.sleep(2)
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_O(bang1, bang2, 2)  # if miss -> give O
                player = "A"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MAIN FUNCTION

def main():
    os.system("clear")

    drawing_board_edges_with_data(1)  # show board A
    ship_location(1)  # Player A puts all his ships

    drawing_board_edges_with_data(2)  # show board B
    ship_location(2)  # Player B puts all his ships

    cleaning_data_in_board()  # cleaning data in both boards. Now the players will be
    shooting()  # within this function there's win_condition


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
main()
