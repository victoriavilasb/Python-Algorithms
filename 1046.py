# -*- coding: utf-8 -*-

linha = input().split(" ")
a, b=linha

#Jogo começou em um dia e terminou no outro
if int(a)==int(b):
    print("O JOGO DUROU 24 HORA(S)")
    
elif int(a)>int(b):
    wresultado=(24-int(a))+int(b)
    print("O JOGO DUROU %1.0f HORA(S)" %(wresultado))
    
#Jogo começou em um dia e terminou no mesmo dia
elif int(a)<int(b):
    wresultado=int(b)-int(a)
    print("O JOGO DUROU %1.0f HORA(S)" %(wresultado))