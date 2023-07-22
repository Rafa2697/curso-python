'''Crie um programa que leia a idade e sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos'''
print('-='*20)
print('Cadastre uma pessoa')
print('-='*20)
count = idade_count = mulher_count = homem_count = idade = 0
sexo = ''
while True:
    idade = int(input('Qual é sua Idade? '))
    sexo = str(input('Qual é seu sexo? [M/F]')).lower()[0]
    if idade > 18:
        idade_count = idade_count + 1
    if sexo == 'm':
        homem_count = homem_count + 1
    if sexo == 'f' and idade < 20:
        mulher_count = mulher_count + 1
        print('-='*20)
    conti = str(input('Quer continuar? [S/N]')).lower()[0]
    print('-='*20)
    if conti == 's':
        print('Cadastre outra pessoa')
    elif conti == 'n':
        break
    else:
        print('Valo invalido')
print(f'Total de pessoas com mais de 18 anos: {idade_count}')
print(f'Ao todo temos {homem_count} homens cadastrados')
print(f'E temos {mulher_count} mulheres com menos de 20 anos')
    
    