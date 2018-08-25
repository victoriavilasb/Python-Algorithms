# -*- coding: utf-8 -*-

i=0
count=0
media=0
while i<6:
    valor=float(input())
    if valor>0:
        count+=1
        media+=valor
    i+=1
print("%1.0f valores positivos"%(count))
print("%1.1f"%(media/count))
