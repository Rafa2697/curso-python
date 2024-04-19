# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. 

# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.


#entrada
quantidade_passos = int(input())

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

if quantidade_passos > -1: #Adicione uma condição para verificar se a quantidade de passos é positiva.
  if quantidade_passos == 0: #Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
    print("Nenhum passo dado na floresta.")
  else: #Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
    for c in range(0, quantidade_passos+1): 
      if c == 1:
         print(f"explorador: {c} passo")
      elif c == 2:
        print(f"explorador: {c} passo")
      else:
        print(f"explorador: {c} passo")

    
    print(f"a quantidade de passos foi {c}")
    
else:
  print("negativo")
  

