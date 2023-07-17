#refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
'''
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

r1 = float(input("Primeiro segmento: "))
r2 = float(input('segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima PODE FORMAR um triangulo ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmento acima NÃO PODEM formar um triangulo.')
    