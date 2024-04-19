#  para ler e escrever dados em python, utilizamos as seguintes funçoes:
# - input: lê UMA linha com dado(s) de entrada do usuario;
# - print: imprime um texto de saída (outout), pulando linha

#função útil para o calculo do importo (baseado nas aliquotas).
def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100.01 and salario <= 25000):
        aliquota = 0.10
    else:
        aliquota = 0.15
        #TODO Criar as demais condições para as aliquotas de 10.00% e 15.00%.
        return aliquota * salario
    
#lê os valores da entrada:
valor_salario = float(input())
valor_beneficios = float(input())

#calcula o imposto através da função "calcaular_imposto":
valor_imposto = calcular_imposto(valor_salario)
# #calcula e imprime a saída (com 2 casas decimais):
# saida = valor_imposto + valor_beneficios 

print(valor_imposto)


    