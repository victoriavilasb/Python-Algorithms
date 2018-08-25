
# -*- coding: utf-8 -*-
import math
wlinha = input().split(" ")
a, b, c = wlinha

delta = float(b)**2 - (4*float(a)*float(c))

if delta<0 or float(a)==0:
    print("Impossivel calcular")
else:
    R1=(float(b)*(-1)+math.sqrt(delta))/(2*float(a))
    R2=(float(b)*(-1)-math.sqrt(delta))/(2*float(a))
    print("R1 = %0.5f"%(R1))
    print("R2 = %0.5f"%(R2))