# auteurs : Degobert Elisa, Weng Victor
# date : 13/10/2016
# objet : TP 5

from turtle import*

    #>>> pencolor('red')
    #>>> forward(100)
    #>>> penup()
    #>>> goto(0,0)
    #>>> pencolor('green')
    #>>> goto(0,-10)
    #>>> pendown()
    #>>> forward(100)


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
        x=x+1

#Dix carrés alignés    

def Nombre_carres_alignes (ligne,longueur,nombre):
    """
    """
    z=1
    u=145
    penup()
    goto(-150,200)
    pendown()
    while not z==(ligne + 1):
        y=1
        while not y == nombre + 1:
            carre(longueur)
            penup()
            forward(longueur + 5)
            pendown()
            y = y + 1
        penup()
        right(90)
        forward(longueur + 5)
        right(90)
        forward(longueur * nombre + 5 * nombre)
        right(180)
        pendown()
        z=z+1

def nombre_carres_emboites(nombre,longueur):
    """
    """
    left(90)
    x=1
    while not x == nombre + 1:
        carre(longueur)
        longueur = longueur + 10
        x = x + 1

def carres_tournants (n):
    """
    """
    x=1
    left(90)
    angle = 360 // n 
    while not x == n + 1:
        carre(100)
        right(angle)
        right
        x=x+1
def angle_figure_convexe(cote):
    return (180*(cote-2)//(cote))

def polygone_reg_convexe (n,l):
    """
    """
    x = 1
    while not x == n + 1:
        forward(l)
        right(180 + (180*(n-2)//n))
        x = x + 1

def polygone_etoile (n,l,k):
    """
    Procedure qui dessine un polygone etoile.
    CU: n >= 5, k > 0
    """
    x = 1
    while not x == n + 1:
        right(360/n*k)
        forward(l)
        x = x + 1       #Q1Q2
