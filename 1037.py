# -*- coding: utf-8 -*-

wvalor=float(input())
if 0<=wvalor<=25:
    print("Intervalo [0,25]")
elif 25<wvalor<=50:
    print("Intervalo (25,50]")
elif 50<wvalor<=75:
    print("Intervalo (50,75]")
elif 75<wvalor<=100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")