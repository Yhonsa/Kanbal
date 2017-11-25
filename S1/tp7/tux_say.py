# auteurs : Elisa Degobert, Victor Weng
# date : 10/11/2016
# objet : TP 7 d'informatique



TUX = "   \\\n    \\\n        .--.\n       |o_o |\n       |:_/ |\n      //   \\ \\\n     (|     | )\n    /'\_   _/`\\\n    \___)=(___/"

def longueur_max(liste):
    """
    Fonction qui renvoie la longueur maximale des chaînes de caractères d'une liste
    CU: La liste contient au moins une chaine de caractères
    Exemples:
    >>> longueur_max (["Cher-e-s étudiant-e-s,", "", "Vous êtes de bons programmeurs."])
    31
    longueur_max(['weng', "degobert"])
    8
    """
    x = 0
    for c in (liste):
          if x <= len(c):
               x = len(c)
    return x

def tux_say(liste):
    """
    Fonction qui est paramétrée par une liste et qui imprime dans une bulle les chaînes de caractères de la liste.
    CU: aucune
    Exemples:
    >>> tux_say (["Cher-e-s étudiant-e-s,", "", "Vous êtes de bons programmeurs."])
     ---------------------------------
    | Cher-e-s étudiant-e-s,          |
    |                                 |
    | Vous êtes de bons programmeurs. |
     ---------------------------------
       \
        \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/
    >>> tux_say ([])
     ---
    | ? |
     ---
       \
        \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/
    """
    if liste == []:
        print(' --- \n| ? |\n --- ')
    else:
        lmax = longueur_max(liste)
        pointille = ' ' + '-' * (lmax+2) + ' '
        print(pointille)
        x = 0
        for cpt in liste:
            print('| ' + cpt + ' '*(lmax - len(cpt)) + ' |')
        print(pointille)
    print(TUX)
        


def V1(liste):
    """
    Fonction qui est paramétrée par une liste et qui imprime dans une bulle les chaînes de caractères de la liste au centre de la bulle.
    CU: aucune
    Exemples:
    >>> V1 (["Cher-e-s étudiant-e-s,", "", "Vous êtes de bons programmeurs."])
     --------------------------------- 
    |     Cher-e-s étudiant-e-s,      |
    |                                 |
    | Vous êtes de bons programmeurs. |
     --------------------------------- 
       \
        \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/
    """
    if liste == []:
        print(' --- \n| ? |\n --- ')
    else:
        lmax = longueur_max(liste)
        pointille = ' ' + '-' * (lmax+2) + ' '
        print(pointille)
        x = 0
        for cpt in liste:
            li = (lmax - len(cpt))//2
            if li != (lmax - len(cpt))/2:
                print('| ' + ' '*li + cpt + ' '*(li+1) + ' |')
            else:
                print('| ' + ' '*li + cpt + ' '*(li) + ' |')
        print(pointille)
    print(TUX)

#V2
psge1 = "   \\\n    \\\n        ____\n       |    |\n      [======]\n       |U_U |\n       |:_/ |\n      // o \\ \\\n     (|  o  | )\n    /'\_ o _/`\\\n    \___)=(___/"
psge2 = "   \\\n    \\\n        .--.\n       |♥_♥ |\n       |:_/ |\n      //>o<\\ \\\n     (|     | )\n    /'\_   _/`\\\n    \___)=(___/"
psge1_2 = "      ____    \\\n     |    |    \\\n    [======]     .--.\n     | U_U|     |♥_♥ |\n     | \_:|     |:_/ |\n    / / o \\\   //>o<\\ \\\n   ( |  o  |) (|     | )\n  /`\_ o _/'\ /'\_   _/`\\\n  \___)=(___/ \___)=(___/"


from cent_mille import CENT_MILLE_MILLIARDS
from random import randint


#V3
##liste =[]
##for i in range (1,14):
##    R = randint(1*i,10*i)
##    liste = liste + [CENT_MILLE_MILLIARDS[R]]
##V1(liste)

        
#V1+V2+V3
def V4(liste):
    """
    Fonction qui est paramétrée par une liste et qui imprime dans une bulle les chaînes de caractères de la liste au centre de la bulle.
    CU: aucune
    Exemples:
    """
    if liste == []:
        print(' '*10 + ' --- \n| ? |\n --- ')
    else:
        lmax = longueur_max(liste)
        pointille =' '*10+' ' + '-' * (lmax+2) + ' '
        print(pointille)
        x = 0
        for cpt in liste:
            li = (lmax-len(cpt))//2
            if li != (lmax-len(cpt))/2:
                print(' '*10+'| ' + ' '*li + cpt + ' '*(li+1) + ' |')
            else:
                print(' '*10+'| ' + ' '*li + cpt + ' '*(li) + ' |')
        print(pointille)


##poème récité
liste = []
for i in range (1,14):
    R = randint(1*i,10*i)
    liste = liste + [CENT_MILLE_MILLIARDS[R]]
V4(liste)
print(psge1_2)
