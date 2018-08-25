# -*- coding: utf-8 -*-

passo1=str(input())
passo2=str(input())
passo3=str(input())

if passo1=="vertebrado":
    if passo2=="ave":
        if passo3=="carnivoro":
            resultado="aguia"
        else:
            resultado="pomba"
    else:
        if passo3=="onivoro":
            resultado="homem"
        else:
            resultado="vaca"
else:
    if passo2=="inseto":
        if passo3=="hematofago":
            resultado="pulga"
        else:
            resultado="lagarta"
    else:
        if passo3=="hematofago":
            resultado="sanguessuga"
        else:
            resultado="minhoca"
        
print(resultado)