# -*- coding: utf-8 -*-
linha = input().split(" ")
a, b=linha
if int(a)>int(b):
    numero_float = (float(a)/float(b))
    verificador = (numero_float-int(numero_float))*1000000000
else:
    numero_float = (float(b)/float(a))
    verificador = (numero_float-int(numero_float))*1000000000
if verificador!=0:
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")
