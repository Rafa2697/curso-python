#escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem
'''
- O primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um numero: '))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print('O primeiro valor Digitado {} é maior que o segundo valor {}'.format(n1,n2))
elif n2 > n1:
    print('O segundo numero {} é maior que o primeiro numero digitado'.format(n2))
else:
    print("não existe valores maiores, ambos são iguais.")
    