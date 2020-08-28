# EXERCÍCIO 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = int(input('Digite o ângulo que deseja: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, tg))