'''faça um porgrama que leia um numero qualquer e mostre o seu fatorial.

ex 5! = 5x4x3x2x1 = 120'''

numero = int(input('Digite uma numero: '))
c = numero
while c > 0:
    print('{}'.format(c), end=' ')
    c = c-1
    f = c * c

print('fatorial desse numero é {}'.format())
