itens = []


# //TODO: Solicite os itens ao usuário
# Cria um laço de repetição para repetir um input 3 vezes
for i in range(3):
    entrada = input("Por favor, insira um valor: ")
    print(f"Você inseriu: {entrada}")
    itens.append(entrada)

# itens.append("Espada")
# itens.append("Escudo")
# itens.append("Poção")

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")