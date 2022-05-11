import math
figury=[]
liczba_figur=int(float(input().strip()))
for i in range(liczba_figur):
  figury.append(input().split())

def pole_prost(a,b):
  return a*b

def pole_kol(r):
  return math.pi * (r)**2

def pole_trojk(a,b,c):
  p = ((float(a))+(float(b))+(float(c)))/2
  return math.sqrt(p*(p-a)*(p-b)*(p-c))

pole=0
for figura in figury:
  if len(figura)>3:
    print("Błąd: można podać maksymalnie 3 liczby") 
    break
  elif len(figura)==1:
    pole += pole_kol(figura[0])
  elif len(figura)==2:
    pole += pole_prost(figura[0],figura[1])
  elif len(figura)==3:
    pole += pole_trojk(figura[0],figura[1],figura[2])
    
print(round(pole,2))
