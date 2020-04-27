#! /usr/bin/pythonw
from classes.CompteBancaire import CompteBancaire
test = 'test'
print(test)

a = 5
b = 10
if a > 0:
    a += 3
    print("a =",a,"et b =",b)

mot = "lac"
mot = mot[-1]
print(mot)

#Exercice compte bancaire
compte1 = CompteBancaire("Winda", 2000)
compte1.depot(900)
compte1.affichage()