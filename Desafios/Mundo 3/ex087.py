# 87
# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0

# inserir dados
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*20)

# exibir
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[\33[36m{matriz[l][c]:^5}\33[m]', end='')
        # soma dos numeros pares
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]      
    print()
print('-='*20)

# soma da ultima coluna
for l in range(0, 3):
    somacoluna += matriz[l][2]

# # maior elemento da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma dos valores pares é \33[36m{somapar}\33[m.')
print(f'A soma dos valores da terceira coluna é \33[36m{somacoluna}\33[m.')
print(f'O maior valor da segunda linha é \33[36m{maior}\33[m.')
print('-='*20)