"""Kérj be két számot a felhasználótól
Írj eljárást
    számok néven
    melynek a paramétere a feéhszanáló által megadott két szám
    és
    az eljárás kiirja a számokat ezen a két paraméter között.

"""

import ciklusok

a: int = int(input("a: "))

b: int = int(input("b: ")) 
"""A felhasznaló csak olyan b-t tudjon megadni, ami nagyobb mint az a"""
while (a>=b):
    print("B-nek nagyobbnak kell lennie  A-nál")
    b:int = int(input)(f"Adj {a}-nál nagyobbat!")



ciklusok.szamok(a,b)
