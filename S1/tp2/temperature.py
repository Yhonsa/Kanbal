#auteurs : Victor Weng, Elisa Degobert
#date : 22/09/2016
#objet : TP 2 d'informatique

C=20  #température en °C (Q1)
F=9*C/5+32  #température en F (Q2)

print("Une température de",C, "°C correspond à une température de",F,"F.") # (Q3)

F2=75
C2=(5/9)*(F2 - 32)
print("Une température de",F2, "F correspond à une température de",C2,"°C.") # (Q4)

def celsius_en_fahrenheit(C):
    """
    Fonction qui convertit une température en degrés Celsius en Fahrenheit
    Valeur renvoyée: degrés Celsius en fahrenheit
    Exemples :
    >>> celsius_en_fahrenheit(20)
    68.0
    """
    return 9*C/5+32
help(celsius_en_fahrenheit) # (Q5)


def fahrenheit_en_celsius(F):
    """
    Fonction qui convertit une température en Fahrenheit en degrés Celsius
    Valeur renvoyée: fahrenheit en degrés Celsius
    CU : F >= 0
    Exemples :
    >>> fahrenheit_en_celsius(75)
    23.88888888888889
    """
    return (5/9)*(F - 32)   # (Q6)

print(celsius_en_fahrenheit(fahrenheit_en_celsius(75)))     # (Q7)
