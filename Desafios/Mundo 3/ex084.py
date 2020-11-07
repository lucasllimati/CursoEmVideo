# 84
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram B) Uma listagem com as pessoas mais C) Uma listagem com as pessoas mais leves.

auxiliar = list()
pessoas = list()
maior = menor = 0

while True:
    auxiliar.append(str(input('Nome: ')))
    auxiliar.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = auxiliar[1] 
        maior = auxiliar[1]    
    else:
        if auxiliar[1] > maior:
            maior = auxiliar[1]
        if auxiliar[1] < menor:
            menor = auxiliar[1]
    print(maior)
    print(menor)
    pessoas.append(auxiliar[:]) # [:] - copia de auxliar para pessoas
    auxiliar.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('¨'*30)
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo, você cadastrou \33[36m{len(pessoas)}\33[m pessoas.')
print(f'O maior peso foi de \33[36m{maior}\33[m Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'\33[36m{p[0].upper()}\33[m ', end='')
print()
print(f'O menor peso foi de \33[36m{menor}\33[m Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'\33[36m{p[0].upper()}\33[m ', end='')