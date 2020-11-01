# EXERCÍCIO 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow, hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#1 - forma
hi = hypot(co, ca)

#2 - forma
#hi = sqrt(pow(cao, 2) + pow(ca, 2))

#3 - forma
#hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}.'.format(hi))