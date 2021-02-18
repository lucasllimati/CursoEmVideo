# 102
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def linha():
    print('-' * 35)
    print('\tCÁLCULO DE FATORIAL')
    print('-' * 35)

def fatorial(n, show = False):
    fatorial = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= c
    return f'\33[36m{fatorial}\33[m'


# Programa principal
linha()
print(fatorial(5, show=True))