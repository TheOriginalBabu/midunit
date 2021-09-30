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
CONST_ACCEPT = [1,2,3]

print("Welcome to Rock Paper Scissors!")

while(True):
    while(move not in CONST_ACCEPT):
        print("Select your move (1 - Rock, 2 - Paper, 3 - Scissors)")
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




#file = open("ccinfo.txt", mode = "r+")

#dafile = file.read()
#dafile = string(dafile)

# if bool(dafile) == True:
#     print("lol")
#     #SavedCCInfo = file.readlines(1)
# else:
#     print("ohno")
# input(dafile)

# if bool(savedCCInfo) == True:
#     print("Saved Credit Card information detected")
#     print("Your saved credit card info is:",savedCCInfo)
#     input()

# elif bool(savedCCInfo) == False:
#     while (int(ccInfo) - 1000000000000000) < 0:
#         print("Please enter credit card info")
#         ccInfo = input()
#         if (int(ccInfo) - 1000000000000000) > 0:
#             file.write(str(ccInfo))
#         elif (int(ccInfo) - 1000000000000000) < 0:
#             print("invalid cc number")