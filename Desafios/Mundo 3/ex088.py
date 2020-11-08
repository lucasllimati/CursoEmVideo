# 88
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# Description
from random import randint
from time import sleep

lista = []
jogos = []
cont = 0
total = 1

print('-' * 33)
print('\tJOGO NA MEGA SENA')
print('-' * 33)

quantjogos = int(input('Quantos jogos você quer que eu sorteie? '))

while total <= quantjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 5, f' SORTEANDO {quantjogos} JOGOS ', '-=' * 5)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print()
print('-=' * 5, f' < BOA SORTE! > ', '-=' * 5)

