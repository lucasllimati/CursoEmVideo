# EXERCÍCIO 55
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0

for i in range (1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < maior:
            menor = peso
        else:
            maior = peso
print('O menor peso foi de {:.2f}Kg.\nO maior peso foi de {:.2f}Kg'.format(menor, maior))
