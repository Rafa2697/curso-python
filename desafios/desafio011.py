#faça um programa que leia a largura e a altura de uma parece em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta ointa uma área de 2m²

altura = float(input('Qual a altura da parece? '))
largura = float(input('Qual a largura da parece? '))

mq = largura * altura
tinta = mq / 2

print('sua parede tem a dimensão de {} x {} e sua área de {}m²'.format(largura,altura,mq))
print('Para pintar essa parede você vai precisar de {} litros de tinta'.format(tinta))