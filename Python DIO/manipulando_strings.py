###############Conhecendo métodos úteis da classe string############
curso = "pYtHoN"

print(curso.upper()) #deixa toda a string e maiuscula 
print(curso.lower()) #deixa toda a string em minuscula
print(curso.title()) #Deixa somente a primeira letra maiscula e as demais minuscula

print(curso.strip() + (".")) #remove os espaços da string
print(curso.lstrip() + ("."))#remove um epaço do lado esquerdo
print(curso.rstrip() + ("."))#remove um epaço do lado direito

#Junções e centralização
print(curso.center(12, '-')) # centraliza a string acrescentando outros caracteres e espaço em branco caso não coloque o caracter.
print('.'.join(curso)) #separa a string letra por letra, usando o . como separador. 


################ interpolação de variáveis ##################

nome = "rafael"
idade = 26
profissao = "programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matrículado no curso de {linguagem}")

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")


