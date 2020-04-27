#! /usr/bin/pythonw
from classes.CompteBancaire import CompteBancaire
from classes.Point import Point

#Exercice compte bancaire
compte1 = CompteBancaire()
compte1.depot(900)
compte1.affichage()

#Exercice point
point1 = Point(10, -34.5)
point1.toString()