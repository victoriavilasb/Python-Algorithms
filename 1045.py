# -*- coding: utf-8 -*-

linha = input().split(" ")
a, b, c=linha

#ordenar os valores
lista=[float(a),float(b),float(c)]
lista=sorted(lista)
a=lista[2]
b=lista[1]
c=lista[0]

if a>=(b+c):
    print("NAO FORMA TRIANGULO")
else: 
    if ((a)**2)==((b)**2+(c)**2):
        print("TRIANGULO RETANGULO")
    if ((a)**2)>((b)**2+(c)**2):
        print("TRIANGULO OBTUSANGULO")
    if ((a)**2)<((b)**2+(c)**2):
        print("TRIANGULO ACUTANGULO")
    if a==b and a==c and b==a:
        print("TRIANGULO EQUILATERO")
    if (a==b and a!=c) or (b==c and c!=a) or (c==a and a!=b):
        print("TRIANGULO ISOSCELES")