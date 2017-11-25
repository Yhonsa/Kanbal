# auteurs : Elisa Degobert, Victor Weng
# date : 06/10/2016
# objet : TP 4 D'informatique

from random import randint

# help(randint)       #Q1
"randint renvoie un nombre entier aléatoire borné entre les deux paramètres entrés."
#>>> randint(0,50)
#9
#>>> randint(-10,10)
#-4


mystere = randint (1, 100)      #Q2

# help(input)
"input permet de demander une valeur à l'utilisateur, elle renvoie une chaîne de caractères"

reponse = input("Entrez une valeur ")
reponse = int(reponse)      #Q3#Q4


reponse=0
essai=0
while reponse!=mystere and essai<7:
    reponse = input("Entrez une valeur ")
    reponse = int(reponse)  
    if reponse < mystere:
        print("plus")
    elif reponse > mystere:
        print("moins")
    essai=essai+1
if reponse==mystere:
    print ("gagné")
else :
    print("perdu")
print()
print("score =",7-essai)        #Q5#Q6



def jeu(e,a,b):
    """
    Fonction qui programme le jeu choisis un nombre.
    CU: e > 0
    Exemples:
    >>> jeu(5,1,10)
    Entrez une valeur 5
    plus
    Entrez une valeur 7
    plus
    Entrez une valeur 9
    gagné

    score = 2
    """
    mystere = randint (a, b)
    reponse = 0
    x = 0
    assert e > 0, "Nombre d'essai doit être supérieur à 0"
    while reponse != mystere and x < e :
        reponse = input("Entrez une valeur ")
        reponse = int(reponse)  
        if reponse < mystere :
            print("plus")
        elif reponse > mystere :
            print("moins")
        x = x + 1
    if reponse == mystere :
        print("gagné")
    else :
        print("perdu")
    print("\nscore =",e-x)      #Q7
