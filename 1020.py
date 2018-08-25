# -*- coding: utf-8 -*-

dias = int(input())
anos = int(dias/365)
resto = dias%365
meses = int(resto/30)
dias = resto%30
print('%1.0f ano(s)'%(anos))
print('%1.0f mes(es)'%(meses))
print('%1.0f dia(s)'%(dias))