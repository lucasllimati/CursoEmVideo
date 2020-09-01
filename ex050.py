# EXERCÍCIO 50
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
cont = 0
soma = 0
for i in range(1, 7):
    num = int(input('Digite o {}º número: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número \33[36mPARES\33[m e a soma foi {}.'.format(cont, soma))
