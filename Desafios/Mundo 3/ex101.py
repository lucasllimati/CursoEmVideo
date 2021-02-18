# 101
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def linha():
    print('_' * 30)

def voto(anonasc):
    from datetime import date
    atual = date.today().year
    idade = atual - anonasc
    if idade < 16:
        return (f'Com {idade} anos: \33[33mNÃO VOTA\33[m.')
    elif 16 <= idade < 18 or idade > 65:
        return (f'Com {idade} anos: \33[32mVOTO OPCIONAL\33[m.')        
    else:
        return (f'Com {idade} anos: \33[31mVOTO OBRIGATÓRIO\33[m.')

# Programa princial
linha()
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))