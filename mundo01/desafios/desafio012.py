#faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


produto = float(input('Digite o valor do produto: '))
novo = produto*5/100

print('o produto que custava {} teve 5% de desconto e agora custa {}'.format(produto, produto - novo ))