# crie um programa que leia o nome completo de uma pessoa e mostre:
'''
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome
'''

nome = str(input("Digite seu nome completo: ")).strip() # vai eliminar os espaçõs de antes e depois

print('Seu nome maiúsculas é {}'.format(nome.upper()))
print('Seu nome minúsculas é {}'.format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' '))) #quantidade de letras menos quantidade de espaços
dividido = nome.split()
print(len(dividido[0]))  