# EXERCÍCIO 4
# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('-=-' * 10, end=' ')
print('JOKENPÔ', end=' ')
print('-=-' * 10)
print('[ 0 ] - PEDRA\n[ 1 ] - PAPEL\n[ 2 ] - TESOURA')
jogador = int(input('Qual sua jogada? '))
item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

if jogador < 0 or jogador > 2 :
    print('\33[31m\tOpção inválida!\33[m')
else:
    print('JO')
    sleep(0.2)
    print('KEN')
    sleep(0.2)
    print('PÔ')
    sleep(0.2)

    print('-=-' * 10)
    print('O Computador jogou: \33[33m{}\33[m'.format(item[computador]))
    print('O Jogaddor jogou: \33[33m{}\33[m'.format(item[jogador]))
    print('-=-' * 10)

    if jogador == 0:
        if computador == 0:
            print('\33[31m\tEMPATE\33[m')
        elif computador == 2:
            print('\33[32m\tJOGADOR\33[m GANHOU!')
        else:
            print('\33[32m\tCOMPUTADOR\33[m GANHOU!')
    elif jogador == 1:
        if computador == 1:
            print('\33[31m\tEMPATE\33[m')
        elif computador == 0:
            print('\33[32m\tJOGADOR\33[m GANHOU!')
        else:
            print('\33[32m\tCOMPUTADOR\33[m GANHOU!')
    elif jogador == 2:
        if computador == 2:
            print('\33[31m\tEMPATE\33[m')
        elif computador == 1:
            print('\33[32m\tJOGADOR\33[m GANHOU!')
        else:
            print('\33[32m\tCOMPUTADOR\33[m GANHOU!')
