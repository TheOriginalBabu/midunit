# author: Izaan Syed
# date: 9/29/2021
# description: midunit assessment, authored by Izaan,
# filename: midunit_izaan.py

# notes: - filename subsection of header is redundant and dumb
#        - date subsection of header is also unnecessary, should be replaced with just date created
import msvcrt
import random


move = 0
score = 0
ccinfo = 0
playcount = 0
gamecontinue = 0
CONST_ACCEPT = [1,2,3]

print("Welcome to Rock Paper Scissors!")

while(True):
    gamecontinue = False
    while(move not in CONST_ACCEPT):
        print("Select your move (1 - Rock, 2 - Paper, 3 - Scissors)")
        print()
        move = int(msvcrt.getch())
        if move not in CONST_ACCEPT:
            print("Invalid input.")
            print()

    if move == 1:
        move = "rock"
    elif move == 2:
        move = "paper"
    elif move == 3:
        move = "scissors"

    aimove = random.choice(["rock","paper","scissors"])

    print("You played",move,".")
    print("The AI played",aimove,".")

    if move == "rock" and aimove == "paper" or move == "paper" and aimove == "scissors" or move == "scissors" and aimove == "rock":
        print("You lost.")
    elif move == aimove:
        print("You tied with the A.I.")
    elif move == "rock" and aimove == "scissors" or move == "paper" and aimove == "rock" or move == "scissors" and aimove =="paper":
        score = score + 1
        print("You won!")
        print("Your new score is",score)
        
    playcount = playcount + 1
    print()

    if playcount == 1:
        while (int(ccinfo) - 1000000000000000) < 0:
            print("Please enter valid credit card info to continue")
            ccinfo = input()
            if int(ccinfo) - 1000000000000000 < 0 or int(ccinfo) - 10000000000000000 > 0:
                print(int(ccinfo) - 1000000000000000)
                print("invalid cc number")

    print()
    print("Cost to continue play: $",playcount - 0.01)
    print("Would you like to continue play? Y/N")

    while(gamecontinue not in [b"n",b"y"]):
        gamecontinue = msvcrt.getch()
        if gamecontinue == b"n":
            exit()

    print()

    


#file = open("ccinfo.txt", mode = "r+")

#infofile = file.read()
#infofile = string(dafile)

# if bool(infofile) == True:
#     SavedCCInfo = file.readlines(1)
# else:
#     print("enterccinfo")
#     input(infofile)

# if bool(savedCCInfo) == True:
#     print("Saved Credit Card information detected")
#     print("Your saved credit card info is:",savedCCInfo)
#     input()
