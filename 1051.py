# -*- coding: utf-8 -*-

wsalario=float(input())
wtotal=0

if (wsalario>=0 and wsalario<=2000):
    print("Isento")
elif wsalario>2000 and wsalario<=3000:
    wsalario-=2000
    wimposto=(wsalario)*0.08
    print("R$ %1.2f" %(wimposto))
elif wsalario>3000 and wsalario<=4500:
    wtotal=1000*0.08
    wtotal+=(wsalario-3000)*0.18
    print("R$ %1.2f" %(wtotal))
else:
    wtotal=1000*0.08
    wtotal+=1500*0.18
    wtotal+=(wsalario-4500)*0.28
    print("R$ %1.2f" %(wtotal))
   