#desenvolva um porgrama que leia o primeiro termo e a razão de um PA. No final, mostr os 10 peimeiros dessa progressão.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')