# 80
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for c in range (0, 5):
    num = int(input('Digite um valor: '))
    # lista[len(lista)-1] é igual a lista[-1]
    if c == 0 or num > lista[-1]: # se for o primeiro ou maior que o ultimo
        lista.append(num)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição \33[36m{pos}\33[m da lista...')
                break
            pos += 1
print('-='*30)
print(f'\n\nOs valores digitados em ordem foram \33[36m{lista}\33[m')
