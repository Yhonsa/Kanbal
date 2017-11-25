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


def imprimer_mois(m,a):
    """
    Fonction qui renvoie une impression du calendrier du mois entrée en paramètre.
    CU:1<=m<=12
    Exemples:
    >>> imprimer_mois(9,2016)
        Septembre 2016
    di lu ma me je ve sa
                 1  2  3  
    4  5  6  7  8  9  10 
    11 12 13 14 15 16 17 
    18 19 20 21 22 23 24 
    25 26 27 28 29 30 

    >>> imprimer_mois(7,2017)
        Juillet 2017
    di lu ma me je ve sa
                   1  
     2  3  4  5  6  7  8  
    9  10 11 12 13 14 15 
    16 17 18 19 20 21 22 
    23 24 25 26 27 28 29 
    30 31 

    """
    j=1
    est_date_valide(j,m,a)
    print("   ",nom_mois(m), a)
    print("di","lu","ma","me","je","ve","sa")
    w=nbre_jours(m,a)
    x=1
    if num_jour(x,m,a)==0:
        print(" ",end="")
        print(x, end="  ")
        while x<w:
            x=x+1
            if x<=9:
                print(x, end="  ")
                if x==7:
                    print()
            else:
                print(x, end=" ")
                if x==14 or x==21 or x==28:
                    print()
                    
        print()
    elif num_jour(x,m,a)==1:
        print(" ", end="")
        print(2*" ",x, end="  ")
        while x<w:
            x=x+1
            if x<=9:
                print(x, end="  ")
                if x==6:
                    print()
            else:
                print(x, end=" ")
                if x==13 or x==20 or x==27:
                    print()
        print()
    elif num_jour(x,m,a)==2:
        print(3*"  ",x, end="  ")
        while x<w:
            x=x+1
            if x<=9:
                print(x, end="  ")
                if x==5:
                    print()
            else:
                print(x, end=" ")
                if x==12 or x==19 or x==26:
                    print()
        print()
    elif num_jour(x,m,a)==3:
        print(" ", end="")
        print(4*"  ",x, end="  ")
        while x<w:
            x=x+1
            if x<=9:
                print(x, end="  ")
                if x==4:
                    print()
            else:
                print(x, end=" ")
                if x==11 or x==18 or x==25:
                    print()
        print()
    elif num_jour(x,m,a)==4:
        print("  ", end="")
        print(5*"  ",x, end="  ")
        while x<w:
            x=x+1
            if x<=9:
                print(x, end="  ")
                if x==3:
                    print()
            else:
                print(x, end=" ")
                if x==10 or x==17 or x==24:
                    print()
        print()
    elif num_jour(x,m,a)==5:
        print(" ", end="")
        print(7*"  ",x, end="  ")
        while x<w:
            x=x+1
            if x<=9:
                print(x, end="  ")
                if x==2:
                    print()
                    print(" ", end="")
                elif x==9:
                    print()
            else:
                print(x, end=" ")
                if x==16 or x==23 or x==30:
                    print()
        print()    
    else:
        if num_jour(x,m,a)==6:
            print("  ", end="")
            print(8*"  ",x, end="  ")
            print()
            print(" ", end="")
            while x<w:
                x=x+1
                if x<=9:
                    print(x, end="  ")
                    if x==8:
                        print()
                else:
                    print(x, end=" ")
                    if x==15 or x==22 or x==29:
                        print()
        print()
    print()                     #Q9

def imprimer_année(a):
    """
    Fonction qui renvoie une impression du calendrier de l'année entrée en paramètre.
    CU:aucune
    Exemples:>>> imprimer_année(2016)
    >>> imprimer_année(2016)
        Janvier 2016
    di lu ma me je ve sa
                   1  2  
    3  4  5  6  7  8  9  
    10 11 12 13 14 15 16 
    17 18 19 20 21 22 23 
    24 25 26 27 28 29 30 
    31 


        Février 2016
    di lu ma me je ve sa
        1  2  3  4  5  6  
    7  8  9  10 11 12 13 
    14 15 16 17 18 19 20 
    21 22 23 24 25 26 27 
    28 29 


        Mars 2016
    di lu ma me je ve sa
           1  2  3  4  5  
    6  7  8  9  10 11 12 
    13 14 15 16 17 18 19 
    20 21 22 23 24 25 26 
    27 28 29 30 31 


        Avril 2016
    di lu ma me je ve sa
                   1  2  
    3  4  5  6  7  8  9  
    10 11 12 13 14 15 16 
    17 18 19 20 21 22 23 
    24 25 26 27 28 29 30 



        Mai 2016
    di lu ma me je ve sa
     1  2  3  4  5  6  7  
    8  9  10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 


        Juin 2016
    di lu ma me je ve sa
              1  2  3  4  
    5  6  7  8  9  10 11 
    12 13 14 15 16 17 18 
    19 20 21 22 23 24 25 
    26 27 28 29 30 


        Juillet 2016
    di lu ma me je ve sa
                   1  2  
    3  4  5  6  7  8  9  
    10 11 12 13 14 15 16 
    17 18 19 20 21 22 23 
    24 25 26 27 28 29 30 
    31 


        Août 2016
    di lu ma me je ve sa
        1  2  3  4  5  6  
    7  8  9  10 11 12 13 
    14 15 16 17 18 19 20 
    21 22 23 24 25 26 27 
    28 29 30 31 


        Septembre 2016
    di lu ma me je ve sa
                 1  2  3  
    4  5  6  7  8  9  10 
    11 12 13 14 15 16 17 
    18 19 20 21 22 23 24 
    25 26 27 28 29 30 


        Octobre 2016
    di lu ma me je ve sa
                       1  
     2  3  4  5  6  7  8  
    9  10 11 12 13 14 15 
    16 17 18 19 20 21 22 
    23 24 25 26 27 28 29 
    30 31 


        Novembre 2016
    di lu ma me je ve sa
           1  2  3  4  5  
    6  7  8  9  10 11 12 
    13 14 15 16 17 18 19 
    20 21 22 23 24 25 26 
    27 28 29 30 


        Décembre 2016
    di lu ma me je ve sa
                 1  2  3  
    4  5  6  7  8  9  10 
    11 12 13 14 15 16 17 
    18 19 20 21 22 23 24 
    25 26 27 28 29 30 31
    
    """
    x=1
    while x<13:
        imprimer_mois(x,a)
        x=x+1
        print()     #Q10


