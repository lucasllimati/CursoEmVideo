# 97
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex: escreva(‘Olá, Mundo! Saída: 
# ~~~~~~~~~ 
# Olá Mundo
# ~~~~~~~~~
from os import system
from time import sleep

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


escreva('OLÁ,MUNDO!')
escreva('CURSO EM VÍDEO')
escreva('CURSO DE PYTHON NO YOUTUBE')
escreva('DEIXA O LIKE')
escreva('LUCAS LIMA')

sleep(1)#Timer
system('cls')#Clear screen

while True:
    mensagem = str(input('Digite uma mensagem: '))
    escreva(mensagem)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\33[31mErro! Responda apenas S ou N.\33[m')
    if resp == 'N':
        break