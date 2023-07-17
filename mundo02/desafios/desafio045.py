#Crie um programa que faça o computador jogar jokenpo com você
from random import randint
from time import sleep
print('{:=^40}'.format(' Jokenpô '))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ!!!')
print('-='*11)
print("O computador escolheu {}".format(itens[computador]))
print("Jogador escolher {}".format(itens[jogador]))
print('-='*11)
if computador == 0:#pedra
    if jogador == 0:
        print('Empatou, os dois joragam {}'.format(itens[computador]))
    elif jogador == 1: #papel
        print('O jogador venceu, {} vence de {}'.format(itens[jogador], itens[computador]))
    elif jogador == 2: #tesoura
        print('O computador venceu, {} vence de {}'.format(itens[computador], itens[jogador]))
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #papel
        if jogador == 0:
            print('O computador venceu, {} vence de {}'.format(itens[computador], itens[jogador]))
        elif jogador == 1:
            print('Empate, os dois jogaram {}'.format(itens[computador]))
        elif jogador == 2:
            print('O Jogador venceu, {} vence de {}'.format(itens[jogador], itens[computador]))
        else:
            print('JOGADA INVALIDA!')
elif computador == 2: #tesoura
        if jogador == 0:
            print('O Jogador venceu, {} vence de {}'.format(itens[jogador], itens[computador]))
        elif jogador == 1:
            print('O computador venceu, {} vence de {}'.format(itens[computador], itens[jogador]))
        elif jogador == 2:
            print('Empate, os dois jogaram {}'.format(itens[computador]))
        else:
            print('JOGADA INVALIDA!')
        
        