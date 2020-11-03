# 73
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Altético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
## Outra forma de exibir a lista de times
# print('Lista de times  do Brasileirão: ',end='')
# for t in times:
#     print(t,end=', ')

# print('-=' * 50)
# print(f'Lista de times  do Brasileirão: {times}.')
# print('-=' * 50)
# print(f'Os 5 primeiros são: {times[0:5]}.')
# print('-=' * 50)
# print(f'Os 4 últimos são: {times[-4:]}.')
# print('-=' * 50)
# print(f'Times em ordem alfabética: {sorted(times)}.')
# print('-=' * 50)
# print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
# print('-=' * 50)


# 2° form - with menu
from time import sleep

while True:
    print('-=' * 25)
    print('\t\t\33[32mBRASILEIRÃO\33[m')
    print('-=' * 25)
    opc = (input(
                      '[1] - Mostrar a classificacao\n'
                      '[2] - Mostrar os 5 primeiros\n'
                      '[3] - Mostrar os 4 últimos\n'
                      '[4] - Times em ordem alfabetica\n'
                      '[5] - Posicao da Chapecoense\n'
                      '[6] - Sair\n'
                      'Escolha uma opção: '))
    while opc not in '123456':
        print('Opcao invalida.')
        opc = int(input(
                          '[1] - Mostrar a classificacao\n'
                          '[2] - Mostrar os 5 primeiros\n'
                          '[3] - Mostrar os 4 últimos\n'
                          '[4] - Times em ordem alfabetica\n'
                          '[5] - Posicao da Chapecoense \n'
                          '[6] - Sair\n'
                          'Escolha uma opção: '))
    if opc == '1':
        print('Lista de times  do Brasileirão: ')
        for pos, c in enumerate (times):
            print(f' {pos+1} {c}')
    if opc == '2':
        print('Os 5 primeiros são: ')
        for pos, cont in enumerate (times[0:5]):
            print(f'{pos+1} {cont}')
    if opc == '3':
        print('Os 4 últimos são: ')
        for z4 in (times[-4:]):
            print(f'{z4}')
    if opc == '4':
        print('Times em ordem alfabética: ',end='')
        print(sorted(times))
    if opc == '5':
        print('A Chapecoense está na ',end='')
        for pos, c in enumerate (times):
            if c == 'Chapecoense':
                print(f'{pos+1}ª posição.')
    if opc == '6':
        print('Você escolheu sair do programa.')
        break
    resp = str(input('\nQuer Continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        print('\33[31mOpção inválida\33[m')
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print('\n')
    sleep(0.5)

print('Desligando...')