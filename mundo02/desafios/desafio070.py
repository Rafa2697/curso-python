'''crie um porgram aque leia o nome e preço de varios produtos. O programa devera perguntar para o usuario  vai continuar. NO final, mostre

A) Qual é o total gasto na compra
B) Quantos pedutos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
print('--'*20)
print('COMPRAS')
print('--'*20)
mil = barato = count = totcompra =0
nome = ''
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input('Preço: R$'))
    count = count + 1
    totcompra = totcompra + preco
    if preco > 1000:
        mil = mil + 1
    if count == 1 or preco < barato:
        barato = preco
        nome = produto
    conti = str(input('Quer continuar? [S/N]')).lower()[0]
    if conti == 's':
        print('proximo produto...')
    if conti == 'n':
        break
print(f'total gasto na compra foi {totcompra:.2f}') 
print(f'Temos {mil} produto(s) custando mais de R$1000.00')
print(f'Produto mais barato foi {nome} custando {barato:.2f}')