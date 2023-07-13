#faça um porgrama que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo.

import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a tangente de {:.2f}'. format(angulo, tangente))
