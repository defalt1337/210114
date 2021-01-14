from random import *
def bekerszam(kerdes,also,felso):
    valasz = int(input(kerdes))
    while valasz < also or valasz > felso:
        valasz = int(input(kerdes))
    return valasz
def veletlenszam(also,felso):
    szam = randint(also,felso)
    return szam
"""def kiir(tomb):
    darab = 1
    for i in tomb:
        if darab == 1:
            print(i,end="")
            darab =+ 1
        else:
            print(":",i,sep="",end="")"""
def kiir(tomb):
    print(tomb[0],sep="",end=" ")
    for i in range(1,len(tomb)):
        print(":",tomb[i],sep=" ",end=" ")