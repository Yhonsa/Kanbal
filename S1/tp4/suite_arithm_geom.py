# auteurs : Elisa Degobert, Victor Weng
# date : 06/10/2016
# objet : TP 4 D'informatique

u_0 = 0
u_1 = 1
u_2 = 4     #Q1

def u_terme (n):
    
    """
    Fonction qui renvoie la valeur de la suite Un avec n étant le rang entré paramètre.
    CU : n >= 0
    Exemples:
    >>> u_terme(2)
    4
    >>> u_terme(1)
    1
    """
    assert n >= 0, 'n doit être supérieur ou égal à 0'
    u_n = 0
    x = 0
    while x < n :
        u_n = 3 * u_n + 1
        x = x + 1
    return u_n      #Q2

def atteint (M):
    """
    Fonction qui renvoie le rang N à partir duquel les termes de la suite sont supérieurs ou égaux à M, entré en paramètre.
    CU : M >= 0
    Exemples:
    >>> atteint(3)
    2
    >>> atteint(4)
    2
    >>> atteint(5)
    3
    """
    assert M >= 0, 'M doit être supérieur ou égal à 0'
    n = 0
    while M > u_terme (n):
        n = n + 1
    return n        #Q3

