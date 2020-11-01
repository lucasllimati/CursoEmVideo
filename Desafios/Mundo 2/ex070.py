# 70
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

# Description
# total ~> sum of values
# quantmil ~>  amount above one thousand reais
# valorbarato ~> cheapest product
# cont ~> counter

print('-' * 35)
print('\tLOJA SUPER BARATÃO')
print('-' * 35)
total = quantmil = valorbarato = cont = 0
nomebarato = ' '

while True:
    print('\n')
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        quantmil += 1
    if valorbarato > preco or cont == 1:
        nomebarato = produto
        valorbarato = preco        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R$ \33[32m{total:.2f}\33[m.')
print(f'Temos \33[32m{quantmil}\33[m produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi \33[32m{nomebarato}\33[m  que custa R$ \33[32m{valorbarato:.2f}\33[m.')