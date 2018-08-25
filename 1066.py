# -*- coding: utf-8 -*-

i=0
pares=0
impares=0
positivos=0
negativos=0
while i<5:
    valor=float(input())
    if valor%2==0:
        pares+=1
    else:
        impares+=1
    if valor>0:
        positivos+=1
    elif valor<0:
        negativos+=1
    i+=1
print("%1.0f valor(es) par(es)"%(pares))
print("%1.0f valor(es) impar(es)"%(impares))
print("%1.0f valor(es) positivo(s)"%(positivos))
print("%1.0f valor(es) negativo(s)"%(negativos))