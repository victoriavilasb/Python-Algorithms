# -*- coding: utf-8 -*-

linha = input().split(" ")
a, b, c = linha
pi = 3.14159
area_triangulo=(float(a)*float(c))/2
area_circulo=pi*(float(c)**2)
area_tapezio=((float(a)+float(b))*float(c))/2
area_quadrado=float(b)**2
area_retangulo=float(a)*float(b)

print('TRIANGULO: %1.3f'%(area_triangulo))
print('CIRCULO: %1.3f'%(area_circulo))
print('TRAPEZIO: %1.3f'%(area_tapezio))
print('QUADRADO: %1.3f'%(area_quadrado))
print('RETANGULO: %1.3f'%(area_retangulo))