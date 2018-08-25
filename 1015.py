# -*- coding: utf-8 -*-

import math
ponto_1 = input().split(" ")
ponto_2 = input().split(" ")
p1_x, p1_y=ponto_1
p2_x, p2_y=ponto_2
distancia = math.sqrt((float(p2_x)-float(p1_x))**2+(float(p2_y)-float(p1_y))**2)
print("%1.4f"%(distancia))