# EXERCÍCIO 39
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anonasc = int(input('Digite o seu ano de nascimento: '))
anoatual = date.today().year
anoalist = anonasc + 18
idade = anoatual - anonasc

print('Quem nasceu em \33[33m{}\33[m tem \33[33m{}\33[m anos em \33[33m{}\33[m.'.format(anonasc, idade, anoatual))

if idade > 18:
    print('Você já deveria ter se alistado há \33[36m{}\33[m anos. Seu alistamento foi em \33[36m{}\33[m.'.format(anoatual - anoalist, anoalist))
elif idade == 18:
    print('Você deve se alistar \33[31mIMEDIATAMENTE\33[m.')
else:
    print('Ainda falta \33[32m{}\33[m anos para o alistamento. Seu alistamento será em \33[32m{}\33[m.'.format(anoalist - anoatual, anoalist))
