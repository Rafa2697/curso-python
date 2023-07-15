#escreva um prgrama que pergunte o salário de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$1.250,00, calcule um aumento de 10%. Para os inferioresou iguis o aumento é de 15%

salario = float(input('Digite seu salario atual: '))
if salario > 1250:
    aumento = salario*10/100
    print('Seu salario agora é de R${:.2f}'.format(aumento+salario))
else:
    aumento = salario*15/100
    print('se salario agora é de {:.2f}'.format(aumento+salario))
    