from random import *
from metodusok import *
from targy import *
targyak =  Targy("teritve", "troli")
print(targyak)
also = bekerszam("Alsóhatár?: ",1,7)
felso = bekerszam("Felsőhatár?: ",5,10)
darab = bekerszam("Darab?: ",1,5)
szamok = []
for i in range(darab):
    #veletlenszam = randint(also,felso)
    szamok.append(veletlenszam(also,felso))
kiir(szamok)

