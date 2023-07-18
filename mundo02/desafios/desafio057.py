#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. caso estej errado, peça a digitação novamente até ter um valor correto. 

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]#strip serve para tirar os espaços feito pelo usuario
while sexo not in 'MmFf':
    sexo = str(input('Digite seu sexo corretamente: [M/F]')).strip().upper()[0]#upper vai deixar tudo em maiusculo e [0 vai pegar a primeira letra da string digitada.]
print('Sexo informado é {}.'.format(sexo))