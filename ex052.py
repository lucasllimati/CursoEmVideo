# EXERCÍCIO 52
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from time import sleep

cont = 0
num = int(input('Digite um número: '))

print('Calculando...')
sleep(1)

for i in range(1, num + 1, 1):
    if num % 1 == 0 and num % i == 0:
        print('\33[33m', end=' ')
        cont += 1
    else:
        print('\33[35m', end=' ')
    print('{}'.format(i), end=' ')
print('\33[m')
print('\nO número \33[36m{}\33[m foi divisível \33[36m{}\33[m vezes.'.format(num, cont))
if cont == 2:
    print('E por isso ele \33[32mÉ PRIMO\33[m.')
else:
    print('E por isso ele \33[31mNÃO É PRIMO\33[m.')