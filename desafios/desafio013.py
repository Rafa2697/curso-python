# faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

salario = float(input('Qual o valor do seu salario? '))

novo = salario*15/100

print('O seu salario de R${:.2f} agora aumentou para R${:.2f}'.format(salario, salario + novo))