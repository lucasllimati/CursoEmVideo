# 95
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totaljogos = int(input(f'Quantas partidas \33[36m{jogador["nome"]}\33[m jogou? '))
    partidas.clear()
    for c in range(0, totaljogos):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\33[31mErro! Responda apenas S ou N.\33[m')
    if resp == 'N':
        break
# header
print('-' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
# table
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual valor? \33[31m(999 para parar)\33[m'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\33[31mErro!\33[m Não existe jogador com o código {busca}! Tente novamente!.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR \33[36m{time[busca]["nome"]}\33[m: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
print('<< \33[31mVOLTE SEMPRE\33[m >>')