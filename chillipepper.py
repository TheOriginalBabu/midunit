# author: Izaan Syed

N = int(input())
T = 0
X = 0

while X < N:
    spice1 = input()
    if spice1 == "Poblano":
        T += 1500
        X += 1
    elif spice1 == "Mirasol":
        T += 6000
        X += 1
    elif spice1 == "Serrano":
        T += 15500
        X += 1
    elif spice1 =="Cayenne":
        T += 40000
        X += 1
    elif spice1 =="Thai":
        T += 75000
        X += 1
    elif spice1 == "Habanero":
        T += 125000
        X += 1

print(T)