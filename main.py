"""Kérj be két számot a felhasználótól
Írj eljárást
    számok néven
    melynek a paramétere a feéhszanáló által megadott két szám
    és
    az eljárás kiirja a számokat ezen a két paraméter között.

"""

import ciklusok

a: int = int(input("Kérj be egy számot:"))
b: int = int(input("Kérj be még egy számot")) 
ciklusok.szamok(a,b)
