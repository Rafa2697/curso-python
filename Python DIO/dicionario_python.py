# pessoa = {"nome": "rafael", "idade": 28} #para criar um dicionario é preciso que as chaves sejam imutaveis. 
# pessoa_2 = dict(nome="guilherme", idade=29)

# print(pessoa["nome"])
# pessoa["telefone"] = "981317461"
# pessoa_2["nome"] #esta acessando o dado
# pessoa_2["idade"] = 37 #está modificando o dado

# print(pessoa)
# print(pessoa_2)


#estrutura de dicionario aninhada
contatos = {
    "rafael@gmail.com": {"nome": "rafael", "telefone": "981317461"},
    "bruna@gmail.com": {"nome": "bruna", "telefone": "1111111111"},
    "veronika@gmail.com": {"nome": "veronika", "telefone": "22222222222"},
    "tamires@gmail.com": {"nome": "tamires", "telefone": "333333333333"},
}

# print(contatos["rafael@gmail.com"]["telefone"])

print(contatos.get("motor"))

for chave, valor in contatos.items():
    print(chave, valor)
    

resultado = "rafael@gmail.com" in contatos #True
resultado_2 = "lugar" in contatos["bruna@gmail.com"] #True

# print(resultado)
# print(resultado_2)
# #metodos
# {}.fromkeys # usado para criar chaves criar uma chave sem vincular nem um valor ou colocar algum valor padrão. 
# {}.clear #limpa o dados do dicionario
# {}.copy #cria uma copia de um dicionario
# {}.get #uma das formas de acessar um valor dentro do dicionario
# {}.pop #serve para remover um valor de uma chave
# {}.popitem #retira os itens na sequência sem apontar uma chave
# {}.setdefault #adiciona um valor caso ele não exista
# {}.update #atualiza uma chave existente, caso não exista irá adicionar um novo dicionario. 
# {}.values #retorna somente os valores
