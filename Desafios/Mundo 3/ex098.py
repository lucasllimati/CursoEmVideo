# 98
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada.

from time import sleep

def linha():
    print('-=' * 20)


def contador(inicio, fim, passo):
    linha()
    print(f'Contagem de \33[32m{inicio}\33[m até \33[32m{fim}\33[m de \33[32m{passo}\33[m em \33[32m{passo}\33[m')
    sleep(1.0)

    # se negativo
    if passo < 0:
        passo *= -1
    # se for 0 / nulo
    if passo == 0:
        passo = 1
    # se inicio for menor que fim
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'\33[36m{cont}\33[m  ', end='', flush='True')
            sleep(0.5)
            cont += passo
        print('\33[31mFIM!\33[m')
    # se fim for menor que inicio
    else:
        cont = inicio
        while cont >= fim:
            print(f'\33[36m{cont}\33[m  ', end='', flush='True')
            sleep(0.5)
            cont -= passo
        print('\33[31mFIM!\33[m')


# Programa principal
contador(0, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim   : '))
pas = int(input('Passo : '))
contador(ini, fim, pas)