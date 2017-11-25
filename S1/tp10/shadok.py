# auteurs : Elisa Degobert, Victor Weng
# date : 24/11/2016
# objet : TP 10 d'informatique



GA = chr(0x004F)

BU = chr(0x2212)

ZO = chr(0x2A3C)

MEU = chr(0x25FF)

ALPHABET_SHADOK = [GA,BU,ZO,MEU]




def entier_en_shadok (nombre):
    """
    Fonction qui renvoie l'écriture shadok de l'entier passé en paramètre.
    CU: nombre est positif ou nul
    Exemples:
    >>> entier_en_shadok (0)
    'O'
    >>> entier_en_shadok (1)
    '−'
    >>> entier_en_shadok (2)
    '⨼'
    >>> entier_en_shadok (3)
    '◿'
    >>> entier_en_shadok (18)
    '−O⨼'
    """
    res = ''
    quotient = nombre
    while quotient >= 4:
        reste = quotient%4
        quotient = quotient//4
        res = str(ALPHABET_SHADOK[reste]) + res
    res = str(ALPHABET_SHADOK[quotient]) + res
    return res
    
# L'écriture shadok de 2014 est : −◿◿−◿⨼



def chiffre_shadok_entier(shadok):
    """
    Fonction qui renvoie un chiffre en base 10 du chiffre shadok correspondant.
    CU : shadok est un caractère appartenant à l'alphabet shadok
    Exemples:
    >>> chiffre_shadok_entier(BU)
    1
    """
    cpt = 0
    for i in ALPHABET_SHADOK:
        if i == shadok:
            return cpt
        cpt = cpt +1




def shadok_en_entier(shadok):
    """
    Fonction qui renvoie le nombre correspondant à une écriture shadok.
    CU: shadok est un nombre positif ou nul (en shadok)
    Exemples:
    >>> shadok_en_entier(GA)
    0
    >>> shadok_en_entier(BU)
    1
    """
    res = 0
    for i in shadok:
            res= res * 4 + chiffre_shadok_entier(i)
    return res


# L'entier correspondant au nombre écrit − ⨼ O ◿ est 99.



##>>> shadok_en_entier (MEU*4)
##255
##>>> int(0b11111111)
##255




def octet_en_shadok (entier):
    '''
    Fonction qui renvoie l'écriture shadok avec exactement quatre chiffres d'un entier représentable sur un octet.
    CU: entier est un nombre positif compris entre 0 et 255
    Exemples:
    >>> octet_en_shadok(0)
    'OOOO'
    >>> octet_en_shadok(255)
    '◿◿◿◿'
    >>> octet_en_shadok(65)
    '−OO−'
    '''
    assert 0 <= entier <= 255, "un octet est compris entre 0 et 255"
    res= entier_en_shadok (entier)
    while len (res)!=4:
        res='O'+res
    return res



# La chaine de caractères qui code 'e' en shadok est −⨼−−



def code_car_en_shadok(char):
    """
    Fonction qui renvoie un caractère ASCII en shadok
    CU: char est un caractère ASCII
    Exemples:
    >>> code_car_en_shadok ('A')
    '−OO−'
    >>> code_car_en_shadok ('e')
    '−⨼−−'
    """
    return entier_en_shadok(ord(char))


    
def code_en_shadok(chaine):
    """
    Fonction qui renvoie en shadok la chaîne de caractères ASCII passée en paramètre.
    CU: chaine est une chaîne de caractères (en ASCII)
    Exemples:
    >>> code_en_shadok('aa')
    '−⨼O−−⨼O−'
    >>> code_en_shadok('shadok')
    '−◿O◿−⨼⨼O−⨼O−−⨼−O−⨼◿◿−⨼⨼◿'
    """
    res = ''
    for c in chaine:
        res = res + code_car_en_shadok(c)
    return res



##>>> chr((2*4+2)*4+2)
##'*'

##>>> chr(((2*4+3)*4+3)*4+1)
##'½'




def decode_car_du_shadok (chaine):
    """
    Fonction qui renvoie le décodage d'une chaîne de quatre caractères shadoks en un caractère ASCII.
    CU: chaine doit être une chaine constituée de 4 caractères étant GA, BU, ZO et MEU.
    Exemples:
    >>> decode_car_du_shadok ('−OO−')
    'A'
    >>> decode_car_du_shadok ('O⨼⨼⨼')
    '*'
    """
    res =0
    for car in chaine:
        res = res*4 + shadok_en_entier(car)
    return chr(res)

def decode_du_shadok (chaine):
    """
    Fonction qui renvoie la chaine de caractères correspondant à la chaine shadok passée en paramètre.
    CU: chaine doit être une chaine composée de l'alphabet shadok
    Exemples:
    >>> decode_du_shadok ('−−−O−⨼⨼−−⨼◿−−⨼◿◿−⨼◿O−⨼−−−⨼◿◿−⨼◿⨼')
    'Timoleon'
    >>> decode_du_shadok ("−O−◿−OO−−OO⨼−−−−−−⨼⨼−O◿◿−O◿−−O−−−−−−")
    'GABUZOMEU'
    """
    res = ''
    a=0
    b=4
    while b<=len(chaine):
        res = res + decode_car_du_shadok(chaine[a:b])
        a = a + 4
        b = b + 4
    return res


##>>> decode_du_shadok ("−O−◿−OO−−OO⨼−−−−−−⨼⨼−O◿◿−O◿−−O−−−−−−")
##'GABUZOMEU'
