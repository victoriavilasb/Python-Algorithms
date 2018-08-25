# -*- coding: utf-8 -*-

segundos = int(input())
horas = int(segundos/3600)
resto = segundos%3600
minutos = int(resto/60)
segundos = segundos%60
print("%1.0f:%1.0f:%1.0f"%(horas,minutos,segundos))