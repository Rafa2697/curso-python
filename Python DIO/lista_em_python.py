########## criação e acesso de dados ##############

# carro = ["Marca", "modelo", 4200000, 2020, 2900, "são paulo", True]

# print(carro[0])
# print(carro[2])
# print(carro)

# matriz = [
    
#     [1,"a",2],
#     ["b",3,2],
#     [1,5,"c"]
# ]

# print(matriz)
# print(matriz[0])
# print(matriz[0][1])
# print(matriz[2][2])


# carros = ["gol", "celta", "uno"]

# for i, carro in enumerate(carros):
#     print(f"{i}: {carro}")
    
# numeros = [1, 30, 21, 2, 9, 65, 34]
# pares = []

# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero) #append adiciona o indice na lista pares.
        
# print(pares)


############# métodos de classe list ###########

# lista = []

# #append
# lista.append(1)
# lista.append("rafael")
# lista.append(True)

# print(lista)

# #clear
# lista.clear()
# print(lista)

# #copy

# lista = [1, "python", [40,30,20]]

# lista.copy()

# print(lista)

# #count
# cores = ["vermelho", "azul", "verde", "azul"]
# cores.count("vermelho")
# cores.count("Azul")
# cores.count("verde")

# print(cores)

# cores.extend(["cinza", "marrom"]) #acrescenta uma lista a outra.

# print(cores)

# #index

# print(cores.index("verde"))

# #pop
# linguagens = ["python", "js", "c", "java"]

# print(linguagens.pop()) #remove o ultimo elemento

#remove
# linguagens.remove("c") # remove o elemento apontado.
# linguagens.reverse() #coloca a lista ao contrario
# linguagens.sort() #vai ordenar de forma alfabetica
# linguagens.sort(reverse=True) #vai ordenar de forma alfabetica ao contrário
# linguagens.sort(key=lambda x: len(x)) #vai ordenar por tamanho da palavra
# linguagens.sort(key=lambda x: len(x), reverse=True) #vai ordenar por tamanho da palavra
# print(linguagens) 
# print(len(linguagens)) #verifica o tamanho da strig ou lista




print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])