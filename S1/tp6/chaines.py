# auteurs : Elisa Degobert, Victor Weng
# date : 20/10/2016
# objet : tp_6


def imprimer_envers(n):
    """
    Fonction qui imprime la chaîne n qu'on lui donne en paramètre en inversant l'ordre des caractères.
    CU: n doit être une chaîne de caractères.
    Exemples:
    >>> imprimer_envers('Timoleon')
    noelomiT
    >>> imprimer_envers('Annabelle')
    ellebannA
    """
    assert type(n) == str, 'n doit être une chaîne de caractères'
    s = n
    x = len(n) - 1
    while x >= 0:
        print (s[x], end='')
        x = x - 1       #Impression à l'envers
        



def miroir(n):
    """
    Fonction qui renvoie une chaîne contenant les caractères de la chaîne n qu'on lui donne en paramètre dans l'ordre inverse.
    CU: n doit être une chaîne de caractères.
    Exemples:
    >>> miroir('Timoleon')
    'noelomiT'
    >>> miroir('Annabelle')
    'ellebannA'
    """
    assert type(n) == str, 'n doit être une chaîne de caractères'
    l = len(n)
    s = n
    m = ''
    for i in range(l):
        m = m + s[l - i - 1]
    return m        #Miroir





def est_palindromique(n):
    """
    Fonction qui renvoie True si la chaîne passée en paramètre est palindromique, sinon False.
    CU: n doit être une chaîne de caractères.
    Exemples:
    >>> est_palindromique('ELLE')
    True
    >>> est_palindromique('ilju')
    False
    """
    return miroir(n) == n         #Q1

def est_palindromique2(n):
    """
    Fonction qui renvoie True si la chaîne passée en paramètre est palindromique, sinon False.
    CU: n doit être une chaîne de caractères.
    Exemples:
    >>> est_palindromique2('ELLE')
    True
    >>> est_palindromique2('ilju')
    False
    """
    assert type(n) == str, 'n doit être une chaîne de caractères'
    l = len(n)
    s = n
    m = ''
    for i in range(l):
        m = m + s[l - i - 1]
    return m == n       #Q2




def my_len(n):
    """
    Fonction qui renvoie la longueur de la chaîne de caractères qu'on lui passe en paramètres.
    CU: n doit être une chaîne de caractères.
    Exemples:
    >>> my_len('Timoleon')
    8
    >>> my_len('Annabelle')
    9
    """
    assert type(n) == str, 'n doit être une chaîne de caractères'
    s = n
    x = 0
    for c in s:
        if c != '':
            x = x + 1
    return x        #Longueur d'une chaîne

def my_len2(n):
    """
    Fonction qui renvoie la longueur de la chaîne de caractères qu'on lui passe en paramètres.
    CU: n doit être une chaîne de caractères.
    Exemples:
    >>> my_len2('Timoleon')
    8
    >>> my_len2('Annabelle')
    9
    """





def sauf(s, i):
    """
    Fonction qui renvoie une chaîne obtenue en supprimant le caractère d'indice i d'une chaîne s, l'indice i et la chaîne s étant passés en paramètres.
    CU: s doit être une chaîne de caractères et 0 <= i < len(s) - 1
    Exemples:
    >>> s = 'Timoleon'
    >>> for i in range(len(s)):
            print(sauf(s, i))

    imoleon
    Tmoleon
    Tioleon
    Timleon
    Timoeon
    Timolon
    Timolen
    Timoleo
    """
    assert 0 <= i < len(s) - 1, 'l\'indice i doit être supérieur à 0 et strictement inférieur à la longueur de s'
    m = ''
    l = len(s)
    for j in range(len(s)):
        if j != i:
            m = m + s[j]
        else:
            m = m + ''
    return m        #suppression d'un caractère




def nbre_occurrences(c, s):
    """
    Fonction qui renvoie le nombre d'occurrences d'un caractère dans une chaîne, le caractère et la chaîne étant passés en paramètre.
    CU: c et s doivent être des chaînes de caractères.
    Exemples:
    >>> nbre_occurrences('o', 'Timoleon')
    2
    >>> nbre_occurrences('y', 'Timoleon')
    0
    >>> nbre_occurrences(' ', 'esope reste ici et se repose')
    5
    """
    x = 0
    for i in range (len(s)):
        if s[i] == c:
            x = x + 1
    return x        #Nombre d'occurrences




def supprime_car(c, s):
    """
    Fonction qui renvoie une chaîne obtenue en supprimant toutes les occurences d'un caractère dans une chaîne, ce caractère et cette chaîne étant passés en paramètres.
    CU: c et s doivent être des chaînes de caractères.
    >>> supprime_car('n', 'Annabelle')
    'Aabelle'
    >>> supprime_car('a', 'Annabelle')
    'Annbelle'
    >>> supprime_car('z', 'Annabelle')
    'Annabelle'
    """
    m = ''
    x = 0
    for i in range (len(s)):
        if s[i] == c:
            m = m + ''
        else:
            m = m + s[i]
    return m        #Suppression des occurences d'un caractère _ Q1


#a = 'esope reste ici et se repose'
#b = supprime_car(' ',a)
#est_palindromique2(b)          #Q2




def remplace_indice (c, i, n):
    """
    Fonction qui remplace le caractère d'un indice donné d'une chaîne de caractères par une autre chaîne de caractères.
    CU: c et n doivent être des chaînes de caractères, 0 <= i < len(c) - 1
    Exemples:
    >>> remplace_indice('Timileon',3,'o')
    'Timoleon'
    >>> remplace_indice('Tixleon',2,'mo')
    'Timoleon'
    """
    assert 0 <= i < len(c) - 1
    return c[:i] + n + c[i + 1:]      #Q1


def remplace_occurrences(c, r, a):
    """
    Fonction qui remplace dans une chaîne donnée toutes les occurences d'un caracère donné par une autre chaîne de caractères.
    CU: c,r et a doivent être des chaînes de caractères.
    Exemples:
    >>> remplace_occurrences ('@ 3 est le neveu de @ 1er.','@','Napoléon')
    'Napoléon 3 est le neveu de Napoléon 1er.'
    >>> remplace_occurrences ('Il fait T','T','froid')
    'Il fait froid' 
    """
    s = c
    p = ''
    for i in range (len(s)):
        if s[i] == r:
            p = p + a
        else:
            p = p + s[i]
    print( p )       #Q2

##test
def reconstruire():
    c=''
    chaine = 'Timoleon'
    i = 0
    while i != len('Timoleon'):
         c = c + chaine[i]
         i = i +1
    print(c)
