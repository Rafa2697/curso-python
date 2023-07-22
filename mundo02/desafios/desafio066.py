'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)'''

n = s = cont = 0
while True:
    n = int(input('Digite um valor(999 para sair): '))
    if n == 999:
        break
    s = s + n
    cont = cont + 1
    
print(f'A soma dos {cont} valores foi {s}')