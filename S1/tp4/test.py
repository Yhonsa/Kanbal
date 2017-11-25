# auteurs : Elisa Degobert, Victor Weng
# date : 06/10/2016
# objet : TP 4 D'informatique

from time import sleep

def compte_a_rebours (n):
    
    """
    Fonction qui affiche le décompte jusque 0 à partir d'un nombre donné en paramètre.
    CU : n > 0, n entier
    Exemples:
    >>> compte_a_rebours(5)
    5
    4
    3
    2
    1
    0
    >>> compte_a_rebours (3)
    3
    2
    1
    0
    """
    assert type(n)==int and n > 0, 'n doit etre un entier supérieur à 0'
    while n >= 0 :
        print(n)
        sleep(1)
        n = n-1         #Q1
