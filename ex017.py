# EXERCÍCIO 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow, hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#Forma 1
hi = hypot(co, ca)

#Forma 2
#hi = sqrt(pow(cao, 2) + pow(ca, 2))

#Forma 3
#hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}.'.format(hi))