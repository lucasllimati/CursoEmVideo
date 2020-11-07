# 81
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados.  B) A lista de valores, ordenada de forma decrescente.  C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    print(end='')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print('¨'*30)
print('-='*30)
print(f'Você digitou \33[36m{len(lista)}\33[m elementos.')
lista.sort(reverse=True)
print(f'O valores em ordem descrescente são \33[36m{lista}\33[m')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5  não foi encontrado lista!')