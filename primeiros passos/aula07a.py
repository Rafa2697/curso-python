#nome = input('qual é seu nome? ')
#print('prazer em te conhcer{:^10}'.format(nome))


n1 = int(input('digite uma valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

teste = 19 // 2
teste2 = 19 % 2
print('a soma é {}, \n o produto é {} e a\n divisão é {:.3f}'.format(s, m, d))#end para não quebrar a linha e \n para quebrar a linha
print('divisao inteira {} e potência {}'.format(di, e))

print(teste, teste2)