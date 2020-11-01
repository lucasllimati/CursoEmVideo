# 69
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

# Description
# maior18 ~> number of people over 18
# homens ~> number of men
# mulheres ~> number of women under 20

maior18 = 0
homens = 0
mulheres = 0

while True:
    print('-+-' * 13)
    print('\tCADASTRO DE PESSOA')
    print('-+-' * 13)
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break        
    print('\n')
print('\n\n')
print('~' * 25)
print('\tESTATÍTICA')
print('~' * 25)
print(f'Total de pessoas com mais de 18 anos: \33[32m{maior18}\33[m.')
print(f'Ao todo temos \33[32m{homens}\33[m homens cadastrados.')
print(f'E temos \33[32m{mulheres}\33[m mulheres com menos de 20 anos.')