# -*- coding: utf-8 -*-

coor_pontos = input().split(" ")
pontox,pontoy = coor_pontos

if float(pontoy)>0<float(pontox):
    print("Q1")
elif float(pontoy)<0<float(pontox):
    print("Q4")
elif float(pontoy)<0>float(pontox):
    print("Q3")
elif float(pontoy)>0>float(pontox):
    print("Q2")
elif float(pontox)==float(pontoy)==0:
    print("Origem")
elif float(pontox)==0:
    print("Eixo Y")
elif float(pontoy)==0:
    print("Eixo X")