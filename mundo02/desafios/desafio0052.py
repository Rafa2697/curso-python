#faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[34m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isos ele não é primo')
    