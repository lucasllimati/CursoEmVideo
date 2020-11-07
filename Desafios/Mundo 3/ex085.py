# 85
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# posição 1   2
lista = [[], []]
valor = 0

for i in range (1, 8):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:  # armazenar na sublista 0 (posição 0 - lista pares)
        lista[0].append(valor)
    else:               # armazenar na sublista 1 (posição 1 - lista impares)
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: \33[36m{lista[0]}\33[m')
print(f'Os valores ímpares digitados foram: \33[36m{lista[1]}\33[m')