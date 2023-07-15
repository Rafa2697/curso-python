#desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.
print('-='*20)
print('Analizador de triângulos')
print('-='*20)
r1 = float(input('primeiro segmento: '))
r2 = float(input("segundo segmento: "))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima não podem formar um triangulo')

