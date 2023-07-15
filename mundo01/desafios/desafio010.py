#crie um programa que leia quanto dinheito uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$1,00 = R$3,27


real = float(input('quantos R$ você tem: '))


dolar = 3.27

compra = real / dolar

print('Com o valor que você tem {}, considerando o preço do dolar {}, você pode comprar {}'.format(real, dolar,compra ))