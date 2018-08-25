# -*- coding: utf-8 -*-

valor = int(input())


cem = int(valor/100)
resto = valor%100

cinquenta = int((resto)/50)
resto=resto%50

vinte = int(resto/20)
resto = resto%20

dez = int(resto/10)
resto = resto%10

cinco = int(resto/5)
resto = resto%5

dois = int(resto/2)
resto = resto%2

print(valor)
print("%1.0f nota(s) de R$ 100,00"%(cem))
print("%1.0f nota(s) de R$ 50,00"%(cinquenta))
print("%1.0f nota(s) de R$ 20,00"%(vinte))
print("%1.0f nota(s) de R$ 10,00"%(dez))
print("%1.0f nota(s) de R$ 5,00"%(cinco))
print("%1.0f nota(s) de R$ 2,00"%(dois))
print("%1.0f nota(s) de R$ 1,00"%(resto))