# 60
# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num =  int(input("Digite um número para calcular seu Fatorial: "))
c = num
fat = 1

# # Forma 1 - utilizando o Math
# from math import factorial
# f = factorial(num)
# print("O fatorial de {} é {}".format(num, f))

# Forma 2 - utilizando o While
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print("{}".format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat = fat * c
    c -= 1
print(fat)
print("\nO fatorial de {}! é \33[32m{}\33[m".format(num, fat))

# # Forma 3 - utilizando o For
# for i in range(num, 0):
#     print("{}".format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     fat = fat * c
#     c -= 1
# print("\nO fatorial de {}! é \33[32m{}\33[m".format(num, fat))