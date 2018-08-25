# -*- coding: utf-8 -*-

peca_1 = input().split(" ")
peca_2 = input().split(" ")
cod_1, num_1, valor_1 = peca_1
cod_2, num_2, valor_2 = peca_2
total = int(num_1)*float(valor_1) + int(num_2)*float(valor_2)
print('VALOR A PAGAR: R$ %1.2f'%(total))