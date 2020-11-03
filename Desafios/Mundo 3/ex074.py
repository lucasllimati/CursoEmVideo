# 74
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteado foram: ',end='')
for n in numeros:
    print(f'\33[36m{n}\33[m',end=' ')
print(f'\nO maior valor sorteado foi: \33[36m{max(numeros)}\33[m')
print(f'O menor valor sorteado foi: \33[36m{min(numeros)}\33[m')