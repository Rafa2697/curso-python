'''
Faça um programa que leia o nome completo de uma pessa, mostrando em seguida o primeiro e o último nome separadamente.
Ex:
->Ana Maria de Souza
->primeiro = Ana
->útimo = Souza
'''


nome = str(input('Digite seu nome completo: ')).strip().split()

print("primeiro nome: {}".format(nome[0]))
print('ultimo nome: {}'.format(nome[len(nome)-1]))
