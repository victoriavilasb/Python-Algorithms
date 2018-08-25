# -*- coding: utf-8 -*-

wquantidade_codigo=input().split(" ")
wcodigo, wqtde=wquantidade_codigo

if wcodigo=="1":
    total=4*float(wqtde)
elif wcodigo=="2":
    total=4.5*float(wqtde)
elif wcodigo=="3":
    total=5*float(wqtde)
elif wcodigo=="4":
    total=2*float(wqtde)
elif wcodigo=="5":
    total=1.5*float(wqtde)
print("Total: R$ %1.2f"%(total))