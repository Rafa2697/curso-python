def exibir_mensagem():
    print("ola mundo")
    
exibir_mensagem()

def exibir_nome(nome="anonimo"):
    print(f"seje bem vindo {nome}")
    
exibir_nome(nome="rafael")
exibir_nome()

def rertonar_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(rertonar_antecessor_sucessor(10))