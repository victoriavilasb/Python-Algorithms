# -*- coding: utf-8 -*-

i=0
count=0
while i<6:
    valor=float(input())
    if valor>0:
        count+=1
    i+=1
print("%1.0f valores positivos"%(count))