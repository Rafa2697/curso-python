#aula sobre manipulação de caracteres


frase = str('  curso em video Python    ')
print(frase)
print(frase[9:14]) #o ultimo valor não entra na contagem
print(frase[9:21:2]) # vai ler pulanod de dois em dois
print(frase[:5]) # vai iniciar em zero até 5
print(frase[15:]) # vai começar do 15 e ir até o final da string
print(frase[9::3]) #mostraria do 9 ao final pulando de 3 em 3
len(frase)# mostra o comprimento 
print(len(frase))
frase.count('o') # mostra quantos 'o' minusculo vai aparecer 
frase.find('deo')# vai indicar a posição que começou a sequencia 'deo'
frase.find('android') # quando a estring não existe o python retorna -1
frase.upper()# a string vai ficar em maiuscula
frase.lower()# deixa a string em minusculo
frase.capitalize()#joga todos os caracreres para minusculo, menos o primeiro caractere
frase.title()# vai transformar todas as palavras com a primeira letra maiuscula
frase.strip()#remove todos os espaços inuteis, somente do começo e do final da string
print(len(frase.strip()))
frase.rstrip()# romove todos os espaços inuteis do lado direito
frase.lstrip()# remove todos os espaço ineteis do lado esquerdo
frase.split()#cada palavra vai ser organizada em uma lista separada
"-".join(frase)
print(frase.replace('Python','Android'))
print('curso' in frase)
dividido = frase.split()
print(dividido)
print(dividido[0])
