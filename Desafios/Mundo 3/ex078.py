# 78
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

menor = maior = 0
listanum = []

print('=-'*30)
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[0]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]            
print('=-'*30)
print(f'O maior valor digitado foi \33[36m{maior}\33[m nas posições ', end='')
for pos, valor in enumerate(listanum):
    if valor == maior:
        print(f'\33[36m{pos}\33[m...', end='')
print()
print(f'O menor valor digitado foi \33[36m{menor}\33[m nas posições ', end='')
for pos, valor in enumerate(listanum):
    if valor == menor:
        print(f'\33[36m{pos}\33[m...', end='')
print()
print(f'Você digitou os valores: \33[36m{listanum}\33[m')
listanum.sort()
print(f'Os valores ordenados são: \33[36m{listanum}\33[m')
print('=-'*30)

