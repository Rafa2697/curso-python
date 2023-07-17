#faça um programa que leia o ano de nascimento de um juvem e informe, de acordo com sua idade:
'''
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- se já passou do tempo de alistamento

seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
genero = int(input('''Qual seu Genero?
                   [ 1 ] Masculino
                   [ 2 ] Feminino
                   ''' ))
if genero == 2:
    print('Você não é obrigado a se alisar.')

elif genero == 1:
    nasc = int(input('Informe sua data de nascimento: '))
    ano_atual = date.today().year
    idade =  ano_atual - nasc
    if idade < 18:
        tempo = 18 - idade
        print('sua idade é {} anos, ainda vai ter que se alistar, faltam {} ano(s) para o alistamento. '.format(idade, tempo))
    elif idade == 18:
        print('Você está com {} anos, chegou a hora de se alistar.'.format(idade))
    else:
        tempo = idade - 18
        print("Você tem {} e passou {} anos do prazo do alistamento".format(idade, tempo))
else:
    print("OPÇÃO INVALIDA.")