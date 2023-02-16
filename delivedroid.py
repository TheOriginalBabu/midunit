# author: Izaan Syed
# Deliv-E-Droid

P = int(input())
C = int(input())

if P < 0:
    P *= -1
if C < 0:
    C *= -1
F = (P * 50) - (C * 10)

if P > C:
    F += 500


print(F)