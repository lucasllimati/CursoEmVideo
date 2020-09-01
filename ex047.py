# EXERCÍCIO 47
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
num = 1

print('NÚMEROS \33[36mPARES\33[m DE 1 ATÉ 50')
print('\33[32mINICIO\33[m', end=' ')
for i in range (1, 51):
    if num % 2 == 0:
        print(num, end=' ')
    num = num + 1
print('\33[31mFIM\33[m')

print('-=' * 30)

num = 1
print('NÚMEROS \33[36mIMPARES\33[m DE 1 ATÉ 50')
print('\33[32mINICIO\33[m', end=' ')
for i in range (1, 51):
    if num % 2 == 1:
        print(num, end=' ')
    num = num + 1
print('\33[31mFIM\33[m')

#OUTRA FORMA
'''
for i in range (2, 51, 2):
    if num % 2 == 0:
        print(num, end=' ')
    num = num + 1
'''