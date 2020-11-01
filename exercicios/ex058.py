# 58
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi? ')

from random import randint

computador = randint(0, 10)
tentativa = 1

jogador = int(input('Qual seu palpites: '))

while computador != jogador:
    if computador < jogador:
        print('Tente um valor\33[31m menor\33[m...',end=' ')
    else:
        print('Tente um valor\33[32m maior\33[m...',end=' ')
    print('Tente novamente')
    jogador = int(input('Qual seu palpites: '))
    tentativa += 1
print('\33[32mParabéns!\33[m Você acertou com \33[32m{}\33[m tentativa(s).'.format(tentativa))
