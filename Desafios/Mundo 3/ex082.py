# 82
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
listaPares = list()
listaImpares = list()

while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print('¨'*30)
for c in range (0, len(lista)):
    if lista[c] % 2 == 0:
        listaPares.append(lista[c])
    else:
        listaImpares.append(lista[c])

# Exemplo - curso em video
# for i, v in enumerate (lista):
#     if v % 2 == 0:
#         listaPares.append(v)
#     else:
#         listaImpares.append(v)
print('-='*30)
print('\t\t\tLista')
print(f'A lista completa é \33[34m{lista}\33[m')
print(f'A lista de pares é \33[36m{listaPares}\33[m')
print(f'A lista de impares é \33[36m{listaImpares}\33[m')
lista.sort()
listaPares.sort()
listaImpares.sort()
print('-='*30)
print('\t\t\tLista ordenada')
print(f'A lista completa ordenada é \33[34m{lista}\33[m')
print(f'A lista de pares ordenada é \33[36m{listaPares}\33[m')
print(f'A lista de impares ordenada é \33[36m{listaImpares}\33[m')
print('-='*30)