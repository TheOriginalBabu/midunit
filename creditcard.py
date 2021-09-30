# author: Izaan Syed
# date: 9/29/2021
# description: midunit assessment, authored by Izaan,
# filename: midunit_izaan.py

# notes: - filename subsection of header is redundant and dumb
#        - date subsection of header is also unnecessary, should be replaced with just date created
import msvcrt
import random


move = "0"
inputmove ="0"
aimove = random.choice(["rock","paper","scissors"])


print("Welcome to Rock Paper Scissors!")
while(inputmove not in [b"1", b"2", b"3"]):
    print("Select your move (1 - Rock, 2 - Paper, 3 - Scissors)")
    inputmove = msvcrt.getch()
    if inputmove not in [b"1", b"2", b"3"]:
        print("Invalid input.")
        print()

if inputmove == b"1":
    move = "rock"
elif inputmove == b"2":
    move = "paper"
elif inputmove == b"3":
    move = "scissors"

print("You played",move,".")
print("The AI played",aimove,".")

if move == "rock" and aimove == "paper" or move == "paper" and aimove == "scissors" or move == "scissors" and aimove == "rock":
    print("You lost.")
elif move == aimove:
    print("You tied with the A.I.")
elif move == "rock" and aimove == "scissors" or move == "paper" and aimove == "rock" or move == "scissors" and aimove =="paper":
    print("You won!")

print(move,aimove)


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