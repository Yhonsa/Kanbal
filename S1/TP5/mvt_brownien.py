# auteurs : Degobert Elisa, Weng Victor
# date : 13/10/2016
# objet : TP 5

from turtle import*
from random import randint

def tortue_sortie(a):
    """
    Prédicat qui renvoie True si la tortue est en dehors du carré dont les côtés ont pour longueur le nombre passé en paramètre, False sinon.
    """
    return -a//2 > xcor() or xcor() > a//2 or -a//2 > ycor() or ycor() > a//2   #Q1

def carre (n):
    """
    Fonction qui ne renvoie rien mais dessine un carré dont la longueur est la valeur entrée en paramètre.
    CU: aucune
    Exemple :
    
    """
    x=1
    while not x==5:
        forward(n)
        right(90)
        x=x+1       #Fonction pour dessiner la limite de mvt_brownien

def mvt_brownien(a):
    """
    Procédure qui simule le mouvement brownien. Il s'arrête quand la tortue dépasse les limites du carré de coté a.
    """
    penup()
    goto(-a//2, a//2)
    pendown()
    pencolor('blue')
    carre(a)
    penup()
    goto(0,0)
    pendown()
    pencolor('red')
    while not tortue_sortie(a):
        right(randint(0,359))
        forward(randint(10,30))         #Q2
