# EXERCÍCIO 54
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoatual = date.today().year
menoridade = 0
maioridade = 0

for i in range(1, 8):
    anonasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    if (anoatual - anonasc) < 21:
        menoridade += 1
    else:
        maioridade += 1
print('Ao todo temos {} maiores de idade e {} menores de idade.'.format(maioridade, menoridade))