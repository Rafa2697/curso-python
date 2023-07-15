#Desenvolva um programa que pergunte a distância de uma viagem de km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

km = float(input('Quantos KM tem sua viagem? '))
if km <=200:
    valor = km * 0.50
    print("O valor da sua viagem fica R${:.2f}".format(valor))
else:
    valor = km * 0.45
    print('o valor da sua viagem fica R${:.2f}'.format(valor))
    