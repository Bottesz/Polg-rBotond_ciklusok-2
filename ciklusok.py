import math
def szamok(a:float,b:float): 
    i:int= math.floor(a) + 1
    while i<b:
        print(i,end=', ')
        i+=1
