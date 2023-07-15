#crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero: '))

dobro = num * 2
triplo = num * 3
#formas de fazer a raiz quadrada
#num**(1/2) ou num**(1/3) para raiz cubica

raiz = num**(1/2)

print('o dobro de {} é {}, o trilo é {} e a raiz quadrada é {}'.format(num, dobro, triplo, raiz))