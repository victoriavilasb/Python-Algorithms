# -*- coding: utf-8 -*-

i=0
count=0
while i<5:
    valor=float(input())
    if valor%2==0:
        count+=1
    i+=1
print("%1.0f valores pares"%(count))
