#Faça um programa que jogue par ou impar com o computador. O jogo só será interronpido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('-='*20)
print('Vamos jogar PAR ou IMPAR')
print('-='*20)
count = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar? [P/I]: ')).lower()[0]
    comp = randint(1,10)
    soma = comp + n
    if pi != 'p' and pi != 'i':
        pi = str(input('Digite [P] para PAR e [I] para IMPAR: '))
    
    if pi == 'p':
        if soma % 2 == 0:
            print('Você ganhou, foi par')
            print('-='*20)
            print(f'Você jogou {n} e o PC jogou {comp} deu PAR')
            print('-='*20)
            count = count + 1
        else:
            print('Voce perdeu, foi impar')
            print(f'GAME OVER! você venceu {count} partida(s)')
            print('-='*20)
            print(f'Você jogou {n} e o PC jogou {comp} deu IMPAR')
            print('-='*20)
            break
    if pi == 'i':
        if soma % 2 != 0:
            print('Você ganhou, foi impar')
            print('-='*20)
            print(f'Você jogou {n} e o PC jogou {comp} deu PAR')
            print('-='*20)
            count = count + 1
        else:
            print('Você perdeu, foi par')
            print(f'GAME OVER! você venceu {count} partida(s)')
            print('-='*20)
            print(f'Você jogou {n} e o PC jogou {comp} deu IMPAR')
            print('-='*20)
            break

    