# def exibir_mensagem():
#     print("ola mundo")
    
# exibir_mensagem()

# def exibir_nome(nome="anonimo"):
#     print(f"seje bem vindo {nome}")
    
# exibir_nome(nome="rafael")
# exibir_nome()

# def rertonar_antecessor_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero + 1
    
#     return antecessor, sucessor

# print(rertonar_antecessor_sucessor(10))


#parâmetros especiais 

#positional only
# def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)
    
# criar_carro("palio", 1998, "GJH7920", marca="fiat", motor="1.0", combustivel="gasolina")

#keyword only
# def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
#          print(modelo, ano, placa, marca, motor, combustivel)
        
# criar_carro(modelo="Palio", ano="1999", placa="GJH7920", marca="fiat", motor="1.0", combustivel="gasolina")

#keyword and positional only
# def criar_carro( modelo, ano, placa, /, *, marca, motor, combustivel):
#          print(modelo, ano, placa, marca, motor, combustivel)
         
# criar_carro("Palio", "1999", "GJH7920", marca="fiat", motor="1.0", combustivel="gasolina")

#objetos de primeira classe

# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     return a / b

# def exibir_resultado(a, b, funcao):
#     resultado = funcao(a, b)
#     print(f"O resultafo da operação entre {a} e {b} é = {resultado}")
    
# exibir_resultado(10, 20, somar)
# exibir_resultado(10, 20, subtrair)
# exibir_resultado(10, 20, multiplicar)
# exibir_resultado(10, 20, dividir)

# op = somar
# print(op(1,24))

# salario = 2000

# def salario_bonus(bonus):
#     global salario
#     salario += bonus
#     return salario

# salario_com_bonus = salario_bonus(500)
# print(salario_com_bonus)

