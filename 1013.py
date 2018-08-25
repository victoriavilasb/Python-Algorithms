# -*- coding: utf-8 -*-

import math

linha= input().split(" ")
a,b,c= linha
maiorab=(int(a)+int(b)+abs(int(a)-int(b)))/2
maiorfinal=(int(maiorab)+int(c)+abs(int(maiorab)-int(c)))/2
print("%1.0f eh o maior"%(maiorfinal) )