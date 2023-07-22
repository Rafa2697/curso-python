'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado(NUMERO INTEIRO) e o programa vai informar quantas cédulas de cada valor serão entregues.

Considere que o caixa posssui cédulas de 50, 20, 10, e 1'''

print('--'*20,'\n CAIXA ELETRONICO \n','--'*20)
num = int(input('Qual valor deseja sacar? '))

while True:
    cinquenta = (num/50)
    num = num % 50
    vinte = (num/20)
    num = num % 20
    dez = (num/10)
    num = num % 10
    um = num
    
    print(cinquenta)
    print(num)
    print(vinte)
    print(num)
    print(dez)
    print(num)
    print(um)
    print(num)
    break

