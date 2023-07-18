#faça um porgrama que leia o peso de 5 pessoas e no final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('informe o {}º peso: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}KG'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))