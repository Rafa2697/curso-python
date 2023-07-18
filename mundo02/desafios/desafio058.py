#melhore o jogo desafio028 onde o computador vai 'pensar' em um numero entre 0 a 10. Só que agora o jogador vai tentar adivinhar até ele acertar, mostrando no final quantos palpites fora necessarios para vencer.

import random

computador = random.randint(0,10)
print('''Sou seu computador... Acabei de pensar em um numero entre 0 e 10.\nSerá que você consegue adivinhar qual foi ?''')
acertou = False
tentativa = 0
while not acertou:
    resposta = int(input('Qual numero o computador pensou ?'))
    tentativa = tentativa + 1
    if resposta == computador:
        acertou = True
    else:
        if resposta < computador:
            print('Mais...Tente novamente')
        else:
            print("Menos...Tente novamente")
print('acertou!, Seu numero de tentativas foi {}'.format(tentativa))3
