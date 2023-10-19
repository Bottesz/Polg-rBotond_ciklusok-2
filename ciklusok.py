import math
def szamok(a:float , b:float): 
  
  if a==b:
    print("Két szám egyenlő")
    return
    if a>b:
        csere:float = a
        a = b
        b = csere
    
    
        i:int= math.ceil(a)
   
while i<b:
        if (i==-1):
            print(i)
else:
        print(i,end=', ')
        i+=1
