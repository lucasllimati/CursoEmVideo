# EXERCÍCIO 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

ang = int(input('Digite o ângulo que deseja: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, tg))