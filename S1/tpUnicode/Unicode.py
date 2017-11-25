from hiragana import *


def est_lettre_majuscule(char):
    """
    Renvoie True si le caractère passé en paramètre est une lettre majuscule de l’alphabet latin non accentuée et False sinon.
    CU: char est un seul caractère
    Exemples:
    >>> est_lettre_majuscule('B')
    True
    >>> est_lettre_majuscule('Z')
    True
    >>> est_lettre_majuscule('z')
    False
    """
    return ord('A') <= ord(char) <= ord('Z')

def est_lettre(char):
    """
    Renvoie True si le caractère passé en paramètre est une lettre de l’alphabet latin non accentuée et False sinon.
    CU: char est un seul caractère
    Exemples:
    """

    return est_lettre_majuscule(char) or ord('a') <= ord(char) <= ord('z')

def est_lettre_française(char):
    """
    """
    vernaculaire = ['à', 'â', 'æ', 'ç', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'Ų', 'ù', 'û', 'ü', 'Ƙ']
    VERNACULAIRE = ['À', 'Â', 'Æ', 'Ç', 'É', 'È', 'Ê', 'Ë', 'Î', 'Ï', 'Ô', 'Œ', 'Ù', 'Û', 'Ü', 'Ÿ']
    return est_lettre(char) or char in vernaculaire or char in VERNACULAIRE

def est_alphanumerique(char):
    """
    """
    return est_lettre(char) or ord('0') <= ord(char) <= ord('9')

## ord('a') - ord('A') = 32 (pour passer de 'A' à 'a', il faut augmenter de 32).

def en_majuscule(chaine):
    """
    """
    res = ''
    for char in chaine:
        if est_lettre(char) and not est_lettre_majuscule(char):
            res = res + chr(ord(char) - 32)
        else:
            res = res + char
    return res

## ord('À') - ord('à') = -32 (pour passer de 'À' à 'à' il faut augmenter de 32)

def en_majuscule_fr(chaine):
    """
    """
    res = ''
    VERNACULAIRE = ['À', 'Â', 'Æ', 'Ç', 'É', 'È', 'Ê', 'Ë', 'Î', 'Ï', 'Ô', 'Œ', 'Ù', 'Û', 'Ü', 'Ÿ']
    for char in chaine:
        if est_lettre_française(char) and not (char in VERNACULAIRE) and not est_lettre_majuscule(char):
            res = res + chr(ord(char) - 32)
        else:
            res = res + char
    return res

def est_hiragana(chaine):
    """
    """
    for c in chaine:
        if not 0x3041 <= ord(c) <= 0x3096:
            return False
    return True

def interprete(chaine):
    """
    """
    res = ''
    for c in chaine:
        res = res + syllabes[ord(c) - 0x3041]
    return res
        
def les_signes():
    """
    Procédure qui renvoie les signes du zodiaques en ASCII.
    Exemple:
    >>> les_signes()
    '♈♉♊♋♌♍♎♏♐♑♒♓'
    """
    res = ''
    for i in range (12):
        res = res + chr(9800 + i)
    return res

def zodiac_sign(nom):
    """
    """
    signes = '♈♉♊♋♌♍♎♏♐♑♒♓'
    signes_lettres = ['bélier', 'taureau', 'gémeaux', 'cancer', 'lion', 'vierge', 'balance', 'scorpion', 'sagittaire', 'capricorne', 'verseau', 'poissons']
    assert nom in signes_lettres, 'le nom doit etre un signe du zodiaque'
    indice = 0
    for c in signes_lettres:
        if nom == c:
            return signes[indice]
        indice = indice + 1

def numerologie(chaine):
    """
    """
    res = 0
    for c in chaine:
        if 1 <= ord(c)-96 <= 9: ##96 = ord('a') - 1
            res = res + ord(c) - 96
        elif 1 <= ord(c) - 105 <= 9: ##105 = ord('j') - 1
            res = res + ord(c) - 105
        else:
            res = res + ord(c) - 114 ##114 = ord('s') - 1
    return res

from fortune import *
from random import randint

def fortune():
    """
    """
    print (fortunes[randint(0,len(fortunes)-1)])

def numero_unicodingologique(chaine):
    """
    """
    res = 0
    for c in chaine:
        res = (res*131 + ord(c)) % len(fortunes)
    return res

from time import asctime

def unicodingologie(nom, zodiac):
    """
    CU: zodiac doit être le signe du zodiaque écrit.
    """
    print (fortunes[numero_unicodingologique(nom + zodiac_sign(zodiac) + str(asctime))])








