nome = str(input("Qual é seu nome? "))
if nome == 'Rafael':
    print("Que nome bonito")
elif nome == 'joão' or nome == 'maria' or nome == 'pedro':
    print("seu nome é bem popular no brasil")
else:
    print("seu nome é nomral")
print("tenha um bom dia {}".format(nome))