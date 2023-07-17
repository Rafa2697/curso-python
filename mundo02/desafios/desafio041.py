#faça um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

'''
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SENIOR
- acima: MASTER '''

from datetime import date

nasc = int(input('Qual ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nasc

if idade <= 9:
    print('{} anos: MIRIM'.format(idade))
elif  idade <= 14:
    print('{} anos: INFANTIL'.format(idade))
elif idade <= 19:
    print('{} anos: JUNIOR'.format(idade))
elif idade <= 25:
    print('{} anos: SENIOR'.format(idade))
else:
    print('{} anos: MASTER'.format(idade))