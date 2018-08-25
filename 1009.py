# -*- coding: utf-8 -*-

nome=str(input())
salario_fixo=float(input())
total_vendas=float(input())
total=salario_fixo+(0.15*total_vendas)
print('TOTAL = R$ %1.2f'%(total))