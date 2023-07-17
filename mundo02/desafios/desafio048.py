#faça um programa que calcule a soma de todos os numeros impares que são multiplo de tres e que se encontre no intervalo de 1 e 500
cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores é {}'.format(cont, soma))
