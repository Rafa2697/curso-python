#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
'''
- 1 para binario
- 2 para octal
- 3 para hexadecimal
'''

num = int(input('Digite uma numero inteiro qualquer: '))
print('''Escolha umas das bases para conversão:
      [ 1 ] converte para BINÁRIO
      [ 2 ] converte para OCTAL
      [ 3 ] converte para HEXADECIMAL''')
opcao = int(input('Sua opção: ')) 
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print("Opção Invalida.")