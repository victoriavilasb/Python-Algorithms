# -*- coding: utf-8 -*-

wlinha = input().split(" ")
a, b, c, d = wlinha

if int(c)>0 and int(d)>0 and int(a)%2==0:
    if int(b)>int(c): 
        if int(d)>int(a):
            if (int(c)+int(d))>(int(a)+int(b)):
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")