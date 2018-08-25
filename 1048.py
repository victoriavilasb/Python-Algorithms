# -*- coding: utf-8 -*-

salario= float(input())
reajuste=0

if salario>0 and salario<=400:
    novo=salario*1.15
    reajuste=novo-salario
    percentual="15 %"
elif salario>400 and salario<=800:
    novo=salario*1.12
    reajuste=novo-salario
    percentual="12 %"
elif salario>800 and salario<=1200:
    novo=salario*1.10
    reajuste=novo-salario
    percentual="10 %"
elif salario>1200 and salario<=2000:
    novo=salario*1.07
    reajuste=novo-salario
    percentual="7 %"
else:
    novo=salario*1.04
    reajuste=novo-salario
    percentual="4 %"

print("Novo salario: %1.2f" %(novo))
print("Reajuste ganho: %1.2f" %(reajuste))
print("Em percentual:",(percentual))