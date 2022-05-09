import math
figury=[]
liczba_figur=int(float(input().strip()))
for i in range(liczba_figur):
  figury.append(input().split())
# print(figury)
pole=0
for figura in figury:
  if len(figura[0:])>3:
    print("Błąd: można podać maksymalnie 3 liczby") 
    break
  elif len(figura[0:])==1:
    wzor_kola=math.pi*(float(figura[0]))**2
    pole+=wzor_kola
  elif len(figura[0:])==2:
    wzor_prostokat=(float(figura[0]))*(float(figura[1]))
    pole += wzor_prostokat
  elif len(figura[0:])==3:
    p=((float(figura[0]))+(float(figura[1]))+(float(figura[2])))/2
    a=(float(figura[0]))
    b=(float(figura[1]))
    c=(float(figura[2]))
    wzor_trojkat=math.sqrt(p*(p-a)*(p-b)*(p-c))
    pole += wzor_trojkat
else:
  print(round(pole,2))