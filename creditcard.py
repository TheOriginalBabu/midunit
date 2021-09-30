import string


file = open("ccinfo.txt", mode = "r+")

dafile = file.read()
#dafile = string(dafile)


if bool(dafile) == True:
    print("lol")
    #SavedCCInfo = file.readlines(1)
else:
    print("ohno")
input(dafile)

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


