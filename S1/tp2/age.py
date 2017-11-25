#auteurs : Victor Weng, Elisa Degobert
#date : 22/09/2016
#objet : TP 2 d'informatique

from datetime import *

ref_an = 1900
ref_mois = 1
ref_jour = 1    # (Q1)

nbre_sec_jour = 86400   # (Q2)
nbre_sec_an = nbre_sec_jour * 365.2425  # (Q3)
nbre_sec_mois = nbre_sec_an / 12    # (Q4)

aujourdhui_an = 2016
aujourdhui_mois = 9
aujourdhui_jour = 22    # (Q5)

nbre_sec_aujourdhui = (aujourdhui_an - ref_an) * nbre_sec_an + (aujourdhui_mois - ref_mois) * nbre_sec_mois + (aujourdhui_jour - ref_jour) * nbre_sec_jour # (Q6)

naissance_an = 1998
naissance_mois = 5
naissance_jour = 3

nbre_sec_naissance = (naissance_an - ref_an) * nbre_sec_an + (naissance_mois - ref_mois) * nbre_sec_mois + (naissance_jour - ref_jour) * nbre_sec_jour  # (Q7)

age = nbre_sec_aujourdhui - nbre_sec_naissance  # (Q8)

def nbre_sec_depuis_1900 (an_p, mois_p, jour_p):
    """
    Fonction qui calcule le nombre approximatif de secondes écoulées entre la date de référence à 0h00 et celle entrée
    CU: an_p >= 1900; 1<=mois_p<=12; 1<=jour_p<=31
    Valeur renvoyée: nombre de secondes depuis 1er janvier 1900
    Exemples:
    >>> nbre_sec_depuis_1900(2016,9,22)
    3683458800.0
    >>> nbre_sec_depuis_1900(1998,5,3)
    3103273080.0
    """
    nbre_sec_depuis_1900 = (an_p - ref_an) * nbre_sec_an + (mois_p - ref_mois) * nbre_sec_mois + (jour_p - ref_jour) * nbre_sec_jour
    return nbre_sec_depuis_1900     # (Q9)

print(nbre_sec_depuis_1900(2016,9,22) - nbre_sec_naissance)     # (Q10)

aujourdhui = date.today()

print(nbre_sec_depuis_1900(aujourdhui.year,aujourdhui.month,aujourdhui.day) - nbre_sec_naissance)   # (Q11)

def age_en_secondes (an,mois,jour):
    """
    Fonction qui calcule l'âge en secondes d'une personne
    CU: an >= 1900; 1<=mois<=12; 1<=jour<=31
    Valeur renvoyée: âge en secondes
    Exemples:
    >>> age_en_secondes(1998,5,3)
    580185720.0
    >>> age_en_secondes(1998,7,20)
    573457428.0
    """
    aujourdhui = date.today()
    sec_depuis_naissance =  (an - ref_an) * nbre_sec_an + (mois - ref_mois) * nbre_sec_mois + (jour - ref_jour) * nbre_sec_jour
    return (nbre_sec_depuis_1900(aujourdhui.year, aujourdhui.month, aujourdhui.day) - sec_depuis_naissance)     # (Q12)




