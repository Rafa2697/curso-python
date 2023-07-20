'''crie um programa que leia varios numeros inteiros pelo teclaro. o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o 999)'''



cont = 0
tot = 0
n = 0
n = int(input("Digite um numero [999] para sair: ".format(cont)))
while n != 999:
    tot = tot + n
    cont = cont+1
    n = int(input("Digite um numero [999] para sair: ".format(cont)))
print('Foram digitados {} numeros e a soma é {}'.format(cont, tot))
