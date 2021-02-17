# 100
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def linha():
    print('-=' * 20)

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush='True')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valor pares de \33[36m{lista}\33[m, temos \33[36m{soma}\33[m.')

#Extra
def somaImpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 1:
            soma += valor
    print(f'Somando os valor impares de \33[36m{lista}\33[m, temos \33[36m{soma}\33[m.')

numeros = list()
sorteia(numeros)
somaPar(numeros)
somaImpar(numeros)