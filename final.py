import time, sys, os, pygame
from termcolor import colored

pygame.init() #for playing sounds (from pygame module)
hit = pygame.mixer.Sound("bomb.wav") #sound when hit
win = pygame.mixer.Sound("clapping.wav") #sound when win
ship = pygame.mixer.Sound("duck.wav") #sound when ship placed
miss = pygame.mixer.Sound("goose.wav") #sound when miss
ship_exists = pygame.mixer.Sound("water_drop.wav") #sound when ship exists
wrong_char = pygame.mixer.Sound("error.wav") #if wrong char

letters = ["A", "B", "C", "D", "E", "F", "G"]  # for validation
digits = [1, 2, 3, 4, 5, 6, 7]  # for validation
dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
tabA = [] #here are Player's A ships
tabB = [] #here are Player's B ships

# EMPTY BOARDS (At the beginning the tables are empty)
#       0       1     2     3     4     5     6     7     8     9     10    11    12    13    14
A = ["║ A ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ A ║"]
B = ["║ B ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ B ║"]
C = ["║ C ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ C ║"]
D = ["║ D ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ D ║"]
E = ["║ E ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ E ║"]
F = ["║ F ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ F ║"]
G = ["║ G ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ G ║"]
Z = [A,B,C,D,E,F,G]

A1 = ["║ A ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ A ║"]
B1 = ["║ B ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ B ║"]
C1 = ["║ C ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ C ║"]
D1 = ["║ D ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ D ║"]
E1 = ["║ E ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ E ║"]
F1 = ["║ F ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ F ║"]
G1 = ["║ G ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ ", "∿", " ║ G ║"]
Z1 = [A1,B1,C1,D1,E1,F1,G1]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FOR CLEANING BOTH BOARDS
def cleaning_data_in_board():
    for x in range(7):
        for i in range(0, 14, 2):
            Z[x][i+1] = "∿"
            Z1[x][i+1] = "∿"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def stringToList(string):
    lis = string.split()
    return lis

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# FOR REFRESHING PLAYER'S A BOARD -> FOR BOTH PLAYERS (a=1 -> PLAYER A)(a=2 -> PLAYER B)
def drawing_board_edges_with_data(a):
    if(a == 1):
        temp = Z
        temp1 = G
        color = "blue"
    elif(a == 2):
        temp = Z1
        temp1 = G1
        color = "green"   
    print(colored("╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗",color, attrs=['bold']))
    print(colored("║   ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║ 6 ║ 7 ║   ║",color, attrs=['bold']))
    print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣",color, attrs=['bold']))

    for i in temp:
        x = ""
        for let in i:
            x += "" + let
        if(i != temp1):
            lis = stringToList(x)
            print(' '.join(
                colored(element, "red", attrs=['bold', 'blink']) if element == "#"
                else colored(element, "white") if element == "∿"
                else colored(element, "red", attrs=['bold']) if element == "X"
                else colored(element, "magenta", attrs=['bold']) if element == "O"
                else colored(element, color, attrs=['bold'])
                for element in lis))
            print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣", color, attrs=['bold']))
        elif(i == temp1):
            lis = stringToList(x)
            print(' '.join(
                colored(element, "red", attrs=['bold', 'blink']) if element == "#"
                else colored(element, "white") if element == "∿"
                else colored(element, "red", attrs=['bold']) if element == "X"
                else colored(element, "magenta", attrs=['bold']) if element == "O"
                else colored(element, color, attrs=['bold'])
                for element in lis))
            print(colored("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣", color, attrs=['bold']))
            print(colored("║   ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║ 6 ║ 7 ║   ║", color, attrs=['bold']))
            print(colored("╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝", color, attrs=['bold']))
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ADDING # TO THE BOARD -> FOR BOTH PLAYERS (z=1 -> PLAYER A)(z=2 -> PLAYER B)
def data_swap(x, y, z):
    if(z == 1):
        temp = Z
    elif(z == 2):
        temp = Z1
    for litera in letters:
        if litera == x:
            temp[dictionary[litera]][y] = "#"
    drawing_board_edges_with_data(z)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# VALIDATION
def if_not_in_letters(x, a):
    if(x not in letters):
        wrong_char.play()
        print(colored("Wrong char!", "red"))
        time.sleep(1.2)
        os.system("clear")
        drawing_board_edges_with_data(a)
        return False
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# VALIDATION
def if_not_in_digits(y, a):
    try:
        y = int(y)
    except ValueError:  # ValueError appears when user inputs not digits
        wrong_char.play()
        print(colored("Wrong char!", "red"))
        time.sleep(1.2)
        os.system("clear")
        drawing_board_edges_with_data(a)
        return False
    if(y not in digits):
        wrong_char.play()
        print(colored("Wrong char!", "red"))
        time.sleep(1.2)
        os.system("clear")
        drawing_board_edges_with_data(a)
        return False
    return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHANGING SMALL LETTERS FOR BIG LETTERS IN USER INPUTS
def toUppercase(lit):
    if lit.isupper(): return lit
    else: return lit.upper()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHECKING SHIP EXISTING -> FOR BOTH PLAYERS
def isShipExists(a, lit, number):
    if(a == 1):
        temp = tabA
    elif(a == 2):
        temp = tabB
    coord = lit+str(number)
    if coord in temp:
        ship_exists.play()
        time.sleep(0.3)
        print(colored("Ship exists already!!!", "red"))
        time.sleep(1.2)
        os.system("clear")
        drawing_board_edges_with_data(a)
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
            if(a == 1): print(colored("PLAYER A", "blue", attrs=['bold']) +" - put the ships in the board")
            elif(a == 2): print(colored("PLAYER B", "green", attrs=['bold']) + " - put the ships in the board")
            print(f"Ship {k}-mast:")
            
            while True: #letter validation
                lit = toUppercase(input(f"Press {z} letter coordinate: "))
                if if_not_in_letters(lit, a):
                    break
            while True: #digit validation
                number = input(f"Press {z} digit coordinate: ")
                if if_not_in_digits(number, a):  
                    number = int(number)
                    break

            if isShipExists(a, lit, number): #if ship is in this point
                continue

            if(a == 1):
                coord = lit+str(number)
                tabA.append(coord)
            if(a == 2):
                coord = lit+str(number)
                tabB.append(coord)

            number = 2*number-1 # we need to translate the user choice, because our board has different coordinates (look at the top)
            os.system("clear")

            data_swap(lit, number, a)
            ship.play()
            time.sleep(0.3)
            z += 1
        s += 1
        k -= 1
        
    if(a == 1):
        print(colored("Player B","green",attrs=['bold']) + " get ready! Now it's your turn!")
        time.sleep(5)
        os.system("clear")
    if(a == 2):
        print(colored("Get ready! Now it's shooting time!","red",attrs=['bold']))
        time.sleep(3)
        os.system("clear")
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# GIVE X (IF HIT) -> FOR BOTH PLAYERS (C=1 -> PLAYER A)(C=2 -> PLAYER B)
def give_X(a, b, c):
    if(c == 1):
        temp = Z
    elif(c == 2):
        temp = Z1
    for lit in letters:
        if lit == a:
            temp[dictionary[lit]][b] = "X"
    drawing_board_edges_with_data(c)  # refresh Player's board
 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# GIVE O (if miss)-> FOR BOTH PLAYERS
def give_O(a, b, c):
    if(c == 1):
        temp = Z
    elif(c == 2):
        temp = Z1
    for lit in letters:
        if lit == a:
            temp[dictionary[lit]][b] = "O"
    drawing_board_edges_with_data(c)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# RULES FOR SHOOTING
def rules():
    color = "magenta"
    print(colored("╔═══╗", color, attrs=['bold']))
    print(colored("║ ∿ ║  -> You may shoot here", color, attrs=['bold']))
    print(colored("╚═══╝", color,attrs=['bold']))
    print(colored("╔═══╗", color,attrs=['bold']))
    print(colored("║ X ║  -> You hit here", color,attrs=['bold']))
    print(colored("╚═══╝", color,attrs=['bold']))
    print(colored("╔═══╗", color, attrs=['bold']))
    print(colored("║ O ║  -> You missed here", color,attrs=['bold']))
    print(colored("╚═══╝", color, attrs=['bold']))

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
            print("SHOOTING! " + colored("Player A", "blue", attrs=['bold']) + " is shooting")
            bang1 = toUppercase(input("Letter coordinate: "))
            if not if_not_in_letters(bang1,1): continue
            bang2 = input("Digit coordinate: ")
            if not if_not_in_digits(bang2,1): continue
            bang2 = int(bang2)
            superBang = bang1 + str(bang2)            
            if(superBang in tabB):  # PLAYER A HIT
                hit.play()
                print(colored("Hit! Try again!", "green", attrs=['bold']))
                time.sleep(1.7)
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_X(bang1, bang2, 1)  # if hit -> give X
                starsA -= 1
                tabB.remove(superBang)
                if(starsA == 0):  # win condition
                    print("WTF?! " + colored("Player A", "blue", attrs=['bold']) + " wins!")
                    win.play()
                    time.sleep(4)
                    sys.exit(0)

            else:  # miss
                miss.play()
                time.sleep(0.4)
                print(colored("MISS! " + colored("Player B","green", attrs=['bold']) + " starts shooting", "red"))
                while True:
                    choice = input("Print Y if you are " + colored("Player B", "green", attrs=['bold']) + ": ")
                    if ((choice == "Y") or (choice == "y")): break
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_O(bang1, bang2, 1)  # if miss -> give O
                player = "B"

        elif(player == "B"):
            os.system("clear")
            drawing_board_edges_with_data(2)
            rules()
            print("SHOOTING! " + colored("Player B", "green", attrs=['bold']) + " is shooting")
            bang1 = toUppercase(input("Letter coordinate: "))
            if not if_not_in_letters(bang1,2): continue
            bang2 = input("Digit coordinate: ")
            if not if_not_in_digits(bang2,2): continue
            bang2 = int(bang2)
            superBang = bang1 + str(bang2)
            if(superBang in tabA):  # PLAYER B HIT
                hit.play()
                print(colored("Hit! Try again!", "green", attrs=['bold']))
                time.sleep(1.7)
                os.system("clear")
                bang2 = 2*bang2 - 1
                give_X(bang1, bang2, 2)  # if hit -> give X
                starsB -= 1
                tabA.remove(superBang)
                if(starsB == 0):  # win condition
                    print("WTF?! " + colored("Player B", "green", attrs=['bold']) + " wins!")
                    win.play()
                    time.sleep(4)
                    sys.exit(0)

            else:  # miss
                miss.play()
                time.sleep(0.4)
                print(colored("MISS! " + colored("Player A","blue", attrs=['bold']) + " starts shooting", "red"))
                while True:
                    choice = input("Print Y if you are "+ colored("Player A","blue", attrs=['bold']) +": ")
                    if choice == "Y"or choice == "y":
                        break
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
