'''melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos, o programa ecerra quando ele disser que quer mostrar mais'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print('Progressão finalizada com {} termos mostrado.'.format(total))