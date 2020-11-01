# 64
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

# Description
# s ~> sum of numbers
# c ~> counter

s = 0
c = 0

print('\33[31mPara parar digite 999\33[m')
print('')
n =  int(input('Digite um número : '))

while n != 999:
    s += n
    c += 1
    n =  int(input('Digite outro número : '))
print('Você digitiou \33[32m{}\33[m números e a soma entre eles foi \33[32m{}\33[m'.format(c, s))