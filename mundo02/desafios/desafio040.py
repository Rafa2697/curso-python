#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

'''
- Média abaixo de 5.0:
reprovado

- media entre 5.0 e 6.9:
recuperação

-media 7.0 ou superior:
aprovado'''

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('sua nota final foi {:1f} REPROVADO'.format(media))
elif media >= 5 and media < 7:
    print('sua nota final foi {:.1f} RECUPERAÇÃO'.format(media))
else:
    print('Sua nota final foi {:.1f} APROVADO'.format(media))
    