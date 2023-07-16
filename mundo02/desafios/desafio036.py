#Escreva um prgrama para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da pestração mensal, sabendo que ela não pode exceder 30% do salario ou então o espréstimo será negado

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salario? '))
anos = int(input('Quantos anos será pago? '))
minimo = salario * 30 /100
prestacao = casa / (anos * 12)
print('Para pagar um casa de R${:.2f} em {}anos'.format(casa, anos), end=' ')
print('a prestação será de  R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONSEDIDO!')
else:
    print('Emprestimo NEGADO!')




