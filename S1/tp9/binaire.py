# auteurs : Elisa Degobert, Victor Weng
# date : 24/11/2016
# objet : TP 9 d'informatique



#Exercice écritures
# 1)  11111011110   
# 2)  3736
# 3) 7de

#Exercice Pair ou impair ?
# Le chiffre des unités d'un nombre binaire vaut 1 si le nombre est impair, il est pair si il est égal à 0.

#Exercice
# 255, 4294967295, 18446744073709551615
# Le plus grand entier que l'on peut écrire avec n bits est égal à 2**n - 1


def mon_bin (nombre):
    '''
    Fonction qui renvoie un nombre passé en paramètre en binaire.
    CU : nombre>=0
    Exemples:
    >>> mon_bin(3)
    '0b11'
    >>> mon_bin (0)
    '0b0'
    '''
    res = ''
    if nombre < 0:
        quotient = abs(nombre)
    else :
        quotient = nombre
    while quotient >= 2:
        reste = quotient%2
        quotient = quotient//2
        res = str(reste) + res
    res = str(quotient) + res
    if nombre < 0:
      return '-0b'+res
    else :
        return '0b'+res

def bin_inv (chaine):
    '''
    Fonction qui renvoie l'entier correspondant à une chaîne en écriture binaire entrée en paramètre
    CU: chaîne est une chaîne de caractères composée de 0 et de 1.
    Exemples:
    >>> bin_inv('0b101111')
    47
    >>> bin_inv('-0b101111')
    -47
    '''
    cpt = 0
    if chaine[0]=='-':
        res = chaine[3:]
    else:
        res = chaine[2:]
    for i in res:
        cpt = cpt*2 + int(i)
    if chaine[0]=='-':
        return -1*cpt
    else:
        return cpt


def Nombre_chiffre(nombre):
    """
    Fonction qui renvoie le nombre hexadécimal correspondant au nombre en base 10
    CU: nombre est compris entre 0 et 15
    Exemples:
    >>> Nombre_chiffre(5)
    '5'
    >>> Nombre_chiffre(15)
    'f'
    """
    chiffres='0123456789abcdef'
    return chiffres[nombre]

def Chiffre_nombre(chaine):
    """
    Fonction qui renvoie le nombre en base 10 correspondant au nombre en base 16
    CU: nombre est compris entre 0 et 15
    Exemples:
    >>> Chiffre_nombre('f')
    15
    >>> Chiffre_nombre('5')
    5
    """
    chiffres='0123456789abcdef'
    liste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    cpt =0
    for i in chiffres :
        if i == chaine:
            return liste[cpt]
        cpt =cpt+1

  
def mon_hex (nombre):
    '''
    Fonction qui renvoie un nombre passé en paramètre en écriture hexadécimale.
    CU : nombre>=0
    Exemples:
    >>> mon_hex(3)
    '0x3'
    >>> mon_hex (0)
    '0x0'
    '''
    res = ''
    
    if nombre < 0:
        quotient = abs(nombre)
    else :
        quotient = nombre
    if quotient < 16:
         res = '0x' + Nombre_chiffre(quotient)
         return res
    while quotient >= 16:
        reste = quotient%16
        quotient = quotient//16
        res = Nombre_chiffre(reste) + res
    res = str(quotient) + res
    if nombre < 0:
      return '-0x'+res
    else :
        return '0x'+res 


def hex_inv (chaine):
    """
    Fonction qui renvoie l'entier correspondant à une chaîne en écriture hexadécimal entrée en paramètre
    CU: chaine doit etre une chaine commençant par 0x
    Exemples:
    >>> hex_inv('0x2f')
    47
    >>> hex_inv('-0x2f')
    -47
    """
    cpt = 0
    if chaine[0]=='-':
        res = chaine[3:]
    else:
        res = chaine[2:]
    for i in res:
        cpt = cpt*16 + Chiffre_nombre(i)
    if chaine[0]=='-':
        return -1*cpt
    else:
        return cpt

def bin_en_hex(chaine):
    """
    Fonction qui convertit une chaine de caractères représentant un nombre entier écrit en binaire en la chaîne hexadécimale représentant le même entier.
    CU: chaine doit être une chaîne de caractères qui commence par 0b
    Exemples:
    >>> bin_en_hex('0b101111')
    '0x2f'
    >>> bin_en_hex('-0b101111')
    '-0x2f'
    """
    cpt = 0
    if chaine[0] == '-':
        binaire = chaine[3:]
        res = '-0b'
    else:
        binaire = chaine[2:]
        res = '0b'
    if len(binaire) % 4 != 0:
        binaire = '0' * (4-(len(binaire))%4) + binaire
    for i in range (len(binaire) // 4):
        res = res + Nombre_chiffre((((int(binaire[cpt]) * 2 + int(binaire[cpt+1])) * 2 + int(binaire[cpt+2])) * 2 + int(binaire[cpt+3])) )
        cpt = cpt + 4
    return res







    
