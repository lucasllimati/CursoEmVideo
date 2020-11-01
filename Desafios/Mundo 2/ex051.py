# EXERCÍCIO 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 40)
print('\t10 TERMOS DE UMA PA')
print('=' * 40)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

print('\33[32mINICIO\33[m', end=' → ')
for num in range(primeiro, decimo + razao, razao):
    print('{}'.format(num), end=' → ')
print('\33[31mACABOU\33[m')