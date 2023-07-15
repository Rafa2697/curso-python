#faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor
print('Digite 3 numeros')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

#verificando qual o menor numero
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
#verificando qual o maior numero
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
    

print('O menor valor digitado foi {} e o maior foi {}'.format(menor,maior))