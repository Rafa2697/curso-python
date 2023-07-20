'''faça um porgrama que leia um numero qualquer e mostre o seu fatorial.

ex 5! = 5x4x3x2x1 = 120'''

numero = int(input('Digite uma numero: '))
c = numero
f = 1
print('Calculando {}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    
    f = f * c
    c = c-1

print('{}'.format( f))
