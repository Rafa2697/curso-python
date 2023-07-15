#escreva um programa que leia a velocidade de um carro, se a velocidade ultrapassar 80km,mostre yma mensagem dizendo que ele foi multado, a multa vai custar 7 reais por cada km acima do limete.

velocidade = int(input('Qual velocidade do carro? '))

if velocidade > 80:
    resto = velocidade - 80
    multa = resto * 7.00
    print("Multado, o valor da multa é de R$ {:.2f}".format(multa))
else:
    print('Você esta dentro do limite de velocidade.')