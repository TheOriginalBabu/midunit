# author: Izaan Syed
# date: 9/29/2021 - 10/1/2021
# description: basic rock paper scissors game, updated to reach midunit 2 criteria
# filename: midunit_izaan.py

# /- notes: -\
# - filename and date subsection of header is redundant and dumb
# - script requires Microsoft Windows to run due to dependence on msvcrt library

# /- changelog: =\
# - added constant variable checker (function)
# - added automated decoder of MSVCRT input (function)
# - fixed bug that would cause program to crash when entering non-integer move selection

# /- Libary import -\ 
import msvcrt
import random

# /- Functions definition -\

def check_CONST_ACCEPT(parameter): # Somewhat useless, runs at end of program to check if constant variables have been altered
    if parameter != True:
        global static1
        static1 = CONST_ACCEPT
    else:
        if CONST_ACCEPT != static1:
            print("Constant Variable Error! Expected", static1, ", received", CONST_ACCEPT)
            exit()

def instantinput():                # Decodes raw MSVCRT input into easy to read
    poll = bytes.decode(msvcrt.getch())
    return poll

# /- Variables definition -\

score = 0
move = False
aimove = False
ccinfo = False
playcount = False
gamecontinue = False

CONST_ACCEPT = ["1","2","3"]
check_CONST_ACCEPT(False)

# -

print("Welcome to Rock Paper Scissors!")    # Welcomes user

while(gamecontinue != "n"):            # Main game loop
    gamecontinue = False                  # If "yes" selected, restart loop and reset continue variable
    while(move not in CONST_ACCEPT):        # Error trapping loop
        print("Select your move (1 - Rock, 2 - Paper, 3 - Scissors)")
        print()
        move = instantinput()  # Gets input for move selection from user, number based selection. Converts string to integer.
        if move not in CONST_ACCEPT:
            print("Invalid input.")
            print()

    if move == 1:                   # Converts integer to string for easier code readability - slows down program a little
        move = "rock"
    elif move == 2:
        move = "paper"
    elif move == 3:
        move = "scissors"

    aimove = random.choice(["rock","paper","scissors"]) # Selects random move (string) for pseudo-A.I.

    print("You played",move,".")
    print("The AI played",aimove,".")                   # Outputs preliminary results to player

    # Main game logic
    if move == "rock" and aimove == "paper" or move == "paper" and aimove == "scissors" or move == "scissors" and aimove == "rock":  # Loss conditions
        print("You lost.")
        print("Your current score is",score)
    elif move == aimove:                                                                                                             # Tie conditions
        print("You tied with the A.I.")
        print("Your current score is",score)
    elif move == "rock" and aimove == "scissors" or move == "paper" and aimove == "rock" or move == "scissors" and aimove =="paper": # Win conditions
        score = score + 1   # Increases score by 1 if won
        print("You won!")
        print("Your new score is",score)

    print()  
    playcount = playcount + 1 # Increases play count by 1 after game

    if playcount == 1:                              # Prompts credit card input to continue (gag based on microtransactions in modern gaming)
        while (int(ccinfo) - 1000000000000000) < 0: # Checks digit count in credit card number provided, error trapped loop
            print("Please enter valid credit card info to continue")
            ccinfo = input()
            if int(ccinfo) - 1000000000000000 < 0 or int(ccinfo) - 10000000000000000 > 0:
                print(int(ccinfo) - 1000000000000000)
                print("Invalid credit  card number inputted. Try again.")

    print("Cost to continue play: $",playcount - 0.01) # Prompts to continue game. Note that only pseudo-billing is implemented.
    print("Would you like to continue play? Y/N")

    while(gamecontinue not in ["n","y"]): # Error trapped loop to get Yes/No input to continue game
        gamecontinue = instantinput()
    print()
    check_CONST_ACCEPT(True)

print("Thank you for playing")
exit()

    


# --- Proof of concpt unimplemented code to store credit card info for future purchases.

#file = open("ccinfo.txt", mode = "r+")

#infofile = file.read()
#infofile = string(infofile)

#if bool(infofile) == True:
#    SavedCCInfo = file.readlines(1)
#else:
#    print("enterccinfo")
#    input(infofile)

#if bool(savedCCInfo) == True:
#    print("Saved Credit Card information detected")
#    print("Your saved credit card info is:",savedCCInfo)
