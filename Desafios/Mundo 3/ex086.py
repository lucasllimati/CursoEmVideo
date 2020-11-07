# 86
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range (0, 3):
    for j in range (0, 3):
        lista[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))
print('-='*10)
for i in range (0, 3):
    for j in range (0, 3):
        print(f'[\33[36m{lista[i][j]:^4}\33[m]', end='')
    print()   