'''
Faça um programa que leia uma frase pelo teclado e monstre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela parece a útilma vez
'''

frase = str(input("Digite uma frase: ")).strip().upper()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))

print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))#find está mostrando onde aparece a letra A pela primeira vez, como a posição inicial é 0, é colocado o +1 para indicar para o usuario onde exatamente esta a letra A.

print('A ultima posição da letra "A" aparece na posição {}'.format(frase.rfind("A")+1))

