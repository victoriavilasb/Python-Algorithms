# -*- coding: utf-8 -*-

valor = float(input())

#NOTAS
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
resto_m = int(resto)%2

#MOEDAS
valor = (valor - int(valor))*100
cinquenta_m = int((valor)/50)
resto=valor%50
vintecinco_m = int(resto/25)
resto = resto%25
dez_m = int(resto/10)
resto = resto%10
cinco_m = int(resto/5)
resto = resto%5


print("NOTAS:")
print("%1.0f nota(s) de R$ 100.00"%(cem))
print("%1.0f nota(s) de R$ 50.00"%(cinquenta))
print("%1.0f nota(s) de R$ 20.00"%(vinte))
print("%1.0f nota(s) de R$ 10.00"%(dez))
print("%1.0f nota(s) de R$ 5.00"%(cinco))
print("%1.0f nota(s) de R$ 2.00"%(dois))
print("MOEDAS:")
print("%1.0f moeda(s) de R$ 1.00"%(resto_m))
print("%1.0f moeda(s) de R$ 0.50"%(cinquenta_m))
print("%1.0f moeda(s) de R$ 0.25"%(vintecinco_m))
print("%1.0f moeda(s) de R$ 0.10"%(dez_m))
print("%1.0f moeda(s) de R$ 0.05"%(cinco_m))
print("%1.0f moeda(s) de R$ 0.01"%(resto))