# -*- coding: utf-8 -*-

coor_pontos = input().split(" ")
x, y, z = coor_pontos

maiorxy=(int(x)+int(y)+abs(int(x)-int(y)))/2
primeiro=(int(maiorxy)+int(z)+abs(int(maiorxy)-int(z)))/2
#print("%1.0f eh o maior"%(maiorfinal) )

if int(x)==primeiro:
    segundo=(int(y)+int(z)+abs(int(y)-int(z)))/2
    if int(y)==segundo:
        terceiro=z
    else:
        terceiro=y  
elif int(y)==primeiro:
    segundo=(int(x)+int(z)+abs(int(x)-int(z)))/2
    if int(z)==segundo:
        terceiro=x
    else:
        terceiro=z
elif int(z)==primeiro:
    segundo=(int(x)+int(y)+abs(int(x)-int(y)))/2
    if int(y)==segundo:
        terceiro=x
    else:
        terceiro=y
print(int(terceiro))
print(int(segundo))
print('%1.0f\n'%(primeiro))

print(x)
print(y)
print(z)