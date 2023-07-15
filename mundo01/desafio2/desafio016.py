#crie um programa que leia qualquer numero real pelo teclado e mostre na tela a sua porção inteira:
# ex: digite um numero: 6.127
# o numero 6.127 tem a parte inteira 6

#import math (importa toda a biblioteca math)
'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''


#mesmo programa sem a biblioteca math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, int(num)))