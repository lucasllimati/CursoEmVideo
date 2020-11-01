# 68
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('-+-' * 13)
print('\tVAMOS JOGAR PAR OU ÍMPAR')
print('-+-' * 13)
print('\nEscolha um valor de 0 até 10')


# Description
# total ~> sum of numbers
# v ~> victory / winning

total = 0
v = 0

while True:
    jogador = int(input('Digite um valor: '))    
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I] ')).strip().upper()[0]
    print(f'Você jogou \33[33m{jogador}\33[m e o computador \33[33m{computador}\33[m. Total de \33[33m{total}\33[m.')
    print(f'DEU PAR' if total %2 == 0 else 'DEU ÍMPAR')

    if tipo == 'P':
        if total % 2 == 0:
            print('\33[32mVocê VENCEU!\33[m')
            v += 1
        else:
            print('\33[31mVocê PERDEU!\33[m')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\33[32mVocê VENCEU!\33[m')
            v += 1
        else:
            print('\33[31mVocê PERDEU!\33[m')
            break
    print('\n\nVamos jogar novamente...')
print(f'\n\n\33[31mGAME OVER!\33[m Você venceu {v} vezes.')