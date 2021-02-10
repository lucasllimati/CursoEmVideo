# 94
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\33[31mErro! Por favor, digite apenas M ou F.\33[m')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\33[31mErro! Responda apenas S ou N.\33[m')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos \33[32m{len(galera)}\33[m pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de \33[32m{media:5.2f}\33[m anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'\33[32m{p["nome"]}\33[m ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = \33[32m{v}\33[m; ', end='')
        print()
print(' << \33[31mENCERRADO\33[m >>')