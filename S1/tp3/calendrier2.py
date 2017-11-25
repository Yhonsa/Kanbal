# auteurs : Elisa Degobert, Victor Weng
# date : 29/09/2016
# objet : TP d'informatique 3

def est_divisible_par(x,y):
    '''
    fonction qui renvoie la valeur True si le premier nombre est divisible par le second. Sinon False
    CU: y != 0
    Exemples:
    >>>est_divisible_par(8,2)
    True    
    >>>est_divisible_par(8,3)
    False
    '''
    assert y != 0, 'Le diviseur doit être différent de 0'
    return x%y==0       #Q1

def est_bissextile(x):
    """
    Fonction qui renvoie la valeur True si la valeur en paramètre est bissextile, sinon False
    CU: aucune
    Exemples:
    >>>est_bissextile(2016)
    True
    >>>est_bissextile(2015)
    False
    """
    return est_divisible_par(x,4) and not est_divisible_par(x,100) or est_divisible_par(x,400)      #Q2


def nbre_jours (m,a):
    """
    Fonction qui renvoie le nombre de jours contenus dans un mois m dans une année a.
    CU: 1<=m<=12
    Exemples:
    >>> nbre_jours(1,2016)
    31
    >>> nbre_jours(2,2015)
    28
    >>> nbre_jours(2,2016)
    29
    """
    assert 1<=m<=12, 'Le mois doit être compris entre 1 et 12'      #Q4
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    else:
        if est_bissextile(a):
            return 29
        else:
            return 28   #Q3

def est_date_valide (j,m,a):
    """
    Fonction qui renvoie la valeur True si la date est valide, sinon False.
    CU: 1<=j<=31, 1<=m<=12
    Exemples :
    >>> est_date_valide(29,2,2016)
    True
    >>> est_date_valide(31,2,2016)
    False
    """
    assert 1<=j<=31, 'Le jour doit être compris entre 1 et 31'
    return j <= nbre_jours(m,a)     #Q5

def corrige_mois(m,a):      
    """
    Fonction qui renvoie la valeur corrigée du mois selon l'algorithme de Delambre
    CU: 1<=m<=12
    Exemples:
    >>> corrige_mois(1,2016)
    3
    >>> corrige_mois(2,2016)
    6
    >>> corrige_mois(9,2015)
    2
    """
    assert 1<=m<=12, 'Le mois doit être compris entre 1 et 12'
    if m==1:
        if est_bissextile(a):
            return 3
        else:
            return 4
    elif m==2:
        if est_bissextile(a):
            return 6
        else:
            return 0
    if m==4 or m==7:
        return 3
    elif m==8:
        return 6
    elif m==3 or m==11:
        return 0
    elif m==5:
        return 5
    elif m==6:
        return 1
    elif m==9 or m==12:
        return 2
    else:
        return 4        #Q6


def num_jour (j,m,a):
    """
    Fonction qui renvoie le numéro du jour dans la semaine correspondant à une date.
    Cu: 1<=j<=31, 1<=m<=12,
    Exemples:
    >>> num_jour(30,9,2016)
    5.0
    >>> num_jour(5,8,2016)
    5.0
    >>> num_jour(3,2,2015)
    2.0
    """
    est_date_valide(j,m,a)
    cd=a%100
    k=int(0.25*cd)
    ab=(a-cd)/100
    q=int(0.25*ab)
    return (k+q+cd+corrige_mois(m,a)+j+2+5*ab)%7        #Q7
    
        
def nom_jour (j,m,a):
    """
    Fonction qui renvoie le nom du jour.
    CU: 1<=j<=31, 1<=m<=12,
    Exemples:
    >>> nom_jour(30,9,2016)
    'Vendredi'
    >>> nom_jour(29,2,2016)
    'Lundi'
    """
    x=num_jour(j,m,a)
    if x==0:
        return "Dimanche"
    elif x==1:
        return "Lundi"
    elif x==2:
        return "Mardi"
    elif x==3:
        return "Mercredi"
    elif x==4:
        return "Jeudi"
    elif x==5:
        return "Vendredi"
    elif x==6:
        return "Samedi"         #Q8
    
def nom_mois (m):
    """
    Fonction qui renvoie le nom du mois entré en paramètre.
    CU: 1<=m<=12
    Exemples:
    >>> nom_mois(2)
    'Février'
    >>> nom_mois(7)
    'Juillet'
    """
    assert 1<=m<=12, 'Le mois doit être compris entre 1 et 12'
    if m==1:
        return "Janvier"
    elif m==2:
        return "Février"
    elif m==3:
        return "Mars"
    elif m==4:
        return "Avril"
    elif m==5:
        return "Mai"
    elif m==6:
        return "Juin"
    elif m==7:
        return "Juillet"
    elif m==8:
        return "Août"
    elif m==9:
        return "Septembre"
    elif m==10:
        return "Octobre"
    elif m==11:
        return "Novembre"
    else:
        return "Décembre"





