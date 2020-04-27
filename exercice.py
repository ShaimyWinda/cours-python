#! /usr/bin/pythonw
from classes.CompteBancaire import CompteBancaire
from classes.Point import Point
from classes.Personne import Personne
from classes.DateDeNaissance import DateDeNaissance
from classes.Employe import Employe
from classes.Chef import Chef

#Exercice compte bancaire
compte1 = CompteBancaire()
compte1.depot(900)
compte1.affichage()
print('\n')
#Exercice point
point1 = Point(10, -34.5)
point1.toString()
print('\n')
#Exercice heritage
personne = Personne("AZIS", "Widad", DateDeNaissance(28,6,1997).toString())
personne.afficher()
print('\n')
employe = Employe("Ilyass", "Math", DateDeNaissance(20,7,1995).toString(), 1265.50)
employe.afficher()
print('\n')
chef = Chef("Ilyan", "Ti", DateDeNaissance(1,7,1980).toString(), 3865.548, "Chef")
chef.afficher()