#escreveva um programa que faça o computador "pensar" um numero entre 0 e 5  e peça para o usuario tentar descobrir qual foi o numero escolhido pelo pc. 
#o programa deverá escrever na tela se o usuario venceu ou perdeu.

import random
from time import sleep

numero = random.randint(0,5)
resposta = int(input('Qual numero entre 0 e 5 foi gerado? '))
print("Processando...")
sleep(3)
if numero == resposta:
    print('Você acertou')
else:
    print('você perdeu, o numero gerado foi {}'.format(numero))
    
print('Obrigado por jogar')