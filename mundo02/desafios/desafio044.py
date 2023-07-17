#elabora um programa que calcule o valor a ser pago por um porduto, considerando o seu preço normal e condição de apagamento:

'''
- à vista dinheiro/cheque: 10% de desconto
- à vista cartão: 5% de deconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
            [ 1 ] à vista dinheiro/cheque
            [ 2 ] à vista cartão
            [ 3 ] 2x no cartão
            [ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual opção? ')) 
if opcao == 1:
    total = preco - (preco * 10/100)
    print('O valor a vista fica {:.2f}'.format(total))
elif opcao == 2:
    total = preco - (preco * 5/100)
    print("O valor com desconto fica {:.2f}".format(total))
elif opcao == 3:
    print('O valor a pagar parcelado é de {:.2f} e o preço total da compra é {:.2f}'.format((preco / 2), preco))
elif opcao == 4:
    total = preco + (preco * 20/100)
    parcelas = int(input('Quantas vezes vocÊ quer parcelar a compra? '))
    print('O valor a pagar parcealdo fica {:.2f} e o total com juros {:.2f}'.format(total / parcelas, total))
else:
    print("opção invalida de pagamento ")