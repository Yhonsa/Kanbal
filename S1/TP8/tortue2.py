# auteurs : Elisa Degobert, Victor Weng
# date : 17/11/2016
# objet : TP 8 d'informatique

from turtle import *

def dessiner (ordres, longueur, angle):
    """
    Fonction qui prend en paramètres une séquence d'ordres, une longueur et un angle et qui trace la séquence ainsi envoyée.
    CU: longueur >=0, angle >= 0, ordres doit être une liste dont less arguments sont 'F', '-', ou '+'
    Exemples:
    >>> dessiner (['F', '-', '-', 'F', '-', '-', 'F', '-', '-'], 100, 60)
    >>> dessiner (['+', 'F', '-', 'F', '-', '-', 'F', '+', '+'], 75, 120)
    """
    assert longueur >= 0 and angle >= 0,"la longueur et l'angle doivent être positifs"
    for i in ordres:
        if i == 'F':
            forward (longueur)
        elif i == '-':
            left (angle)
        elif i == '+':
            right (angle)   #Q1
            

## carré : dessiner(['F','+','F','+','F','+','F'],100,90)
## hexagone régulier : dessiner(['F','+','F','+','F','+','F','+','F','+','F'],100,60)
## maison : dessiner(['F','+','+','+','F','+','+','+','F','+','+','+','F','+','F','+','+','+','+','F'],100,30)
e=['+']*2+['F']
m=['-']*2+['F']
n=['-']+m
o=m+['F']
l=['+']+e
g=3*['F']+5*['+']
h=['-','F','F']
## mouton : dessiner(l*3+['F']+m+['-']+['F']+n*5+['+']+['F']+3*o+5*['+']+2*['F']+m+['F']+e+['F']+2*n+['F','+']+e+['F']+l+['F']+2*n+['F']+e+2*['-']+2*g+['+']+4*['F']+2*h+['F']+h+e+['-','F'],50,30)


def derive (so, r):
    """
    Fonction qui renvoie la dérivation de la première liste passée en paramètre par la seconde
    Cu: so et r sont des listes
    Exemples:
    >>> derive (['F', '+', 'F'],['F', '-', 'F'])
    ['F', '-', 'F', '+', 'F', '-', 'F']
    >>> derive(['F','F'], ['-','+','-'])
    ['-', '+', '-', '-', '+', '-']
    """
    assert type(so) == list and type(r) == list, 'so et r doivent être des listes'
    liste = []
    i = 0
    for c in so:
        if c != 'F':
            liste = liste + [c]
        else:
            liste = liste + r
    return liste


def derive_n (so, r, n):
    """
    Fonction qui renvoie la n-ième dérivation de la première liste passée en paramètre par la seconde
    CU: so et r sont des listes
    Exemples:
    >>> derive_n(['F', '+', 'F'],['F', '-', 'F'],1)
    ['F', '-', 'F', '+', 'F', '-', 'F']
    >>> derive_n(['F', '+', 'F'],['F', '-', 'F'],2)
    ['F', '-', 'F', '-', 'F', '-', 'F', '+', 'F', '-', 'F', '-', 'F', '-', 'F']
    >>> derive_n(['F', '+', 'F'],['F', '-', 'F'],0)
    ['F', '+', 'F']
    """
    assert type(so) == list and type(r) == list, 'so et r doivent être des listes'
    cpt = 0
    liste = list(so)
    while cpt != n:
        liste = derive (liste, r)
        cpt = cpt + 1
    return liste


from random import randint
n = randint(0,5)
speed(0)
# dessiner (derive_n(['F', '-', '-', 'F', '-', '-', 'F', '-', '-'],['F', '+', 'F', '-', '-', 'F', '+', 'F'],n),3**(5-n),60)
# dessiner (derive_n(['F'],['F', '+', 'F', '-', 'F', '-', 'F', '+', 'F'],n),3**(5-n),90)
dessiner (derive_n(['F','F','-','-','F','+','F','-','F','-','F','+','F','-','-','F'],['F', '+', 'F', '-', 'F', '-', 'F', '+', 'F'],4),3**(5-4),90)
