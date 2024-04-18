# letras = set(("a", "b", "c", "a", "r"))  #{"a", "b", "c", "a", "r"} não é possivel alterar o indice no conjunto, mas podemos converter para uma lista.
# letras = list(letras)
# print(letras[1])

# carros = set(("gol", "celta", "palio"))
# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")
    
# conjunto_a = {1, 2, 3}
# conjunto_b = {2, 3, 4, 8, 10, 2, 1}

# conjunto_a.add(32)
# print(conjunto_a)

# print(conjunto_a.union(conjunto_b))
# print(conjunto_a.intersection(conjunto_b))
# print(conjunto_a.difference(conjunto_b))
# print(conjunto_a.symmetric_difference(conjunto_b))
# print(conjunto_a.issuperset(conjunto_b))
# print(conjunto_b.issuperset(conjunto_a))
# print(conjunto_b.isdisjoint(conjunto_a))

# conjunto_b.clear()
# print(conjunto_b)


numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0}

print(numeros)
print(numeros.discard(45))
print(len(numeros))
print(numeros)
