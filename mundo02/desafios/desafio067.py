#faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario. O prgrama será interrompido quando o números solicitado for negativo.

n = 0
while n > -1:
    n = int(input('Digiete um numero para tabuada: '))
    print('-='*15)
    count = 0
    while n > -1:
        count = count + 1
        print(f'{n} x {count} = {n * count}')
        if count == 10:
            break
    print('Programa encerrado')