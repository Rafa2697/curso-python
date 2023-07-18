#estrutura de repetição while
'''c = 1
while c < 10:
    print(c)
    c = c+1
print('fim')
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite uom valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Vecê digitou {} Número pares e {} Números impares!'.format(par,impar))