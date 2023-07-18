'''crie um programa que leia dois valores e mostre em menu na tela:
[ 1 ]somar
[ 2 ]multiplicar
[ 3 ]maior
[ 4 ]novos numeros
[ 5 ]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''
from time import sleep

n1 = int(input('Digite primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] novos numeros
        [5] sair''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('o valor somado entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O valor multiplicado entre {} e {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('-=-'*10)
    sleep(1.5)
print('Fim do programa..')