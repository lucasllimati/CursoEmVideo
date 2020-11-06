# 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('\33[32mValor adicionado com sucesso!\33[m', end='')
    else:
        print('\33[31mValor duplicado! Não será adicionado.\33[m', end='')   
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nQuer continuar? [S/N] ')).upper().strip()[0]
    print('¨'*30)
    if resp == 'N':
        break
print()    
print('-='*30)
lista.sort()
print(f'Você digitou os valores \33[36m{lista}\33[m')
