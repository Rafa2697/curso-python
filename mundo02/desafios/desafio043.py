#desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

'''
- Abaico de 18.5: Abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- Acima de 40: Obesidade mórbida'''

peso = float(input("Qual seu peso? (KG)"))
altura = float(input('Qual sua altura? (M)'))

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso normal')
elif 18.5 <= imc < 25: # imc >= 18.5 and imc <= 25
    print(' O IMC  dessa pessoa é de {:.1f} e está NORMAL'.format(imc))
elif imc >= 25 and imc > 30:
    print('O IMC dessa pessoa é de {:.1f}, está em sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('O IMC dessa pessoa é de {:.1f}, está em OBSIDADE'.format(imc))
else:
    print('O IMC dessa pessoa é {:.1f}, cuidado OBSIDADE MÓRBIDA'.format(imc))