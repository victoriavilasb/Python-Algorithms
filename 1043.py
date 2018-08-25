# -*- coding: utf-8 -*-
linha = input().split(" ")
a, b, c=linha


verificador = False 
# tratando a
if (float(b)+float(c))>float(a)>(float(b)-float(c)):
    if (float(a)+float(c))>float(b)>(float(a)-float(c)):
        if (float(a)+float(b))>float(c)>(float(a)-float(b)):
            verificador=True
if verificador==True:
    print("Perimetro = %1.1f"%(float(a)+float(b)+float(c)))
else:
    trapezio=((float(a)+float(b))*float(c))/2
    print("Area = %1.1f"%(trapezio))