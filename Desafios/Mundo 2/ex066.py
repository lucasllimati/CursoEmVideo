# 66
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

# Description
# s ~> sum of numbers
# c ~> counter

s = 0
c = 0

print('\33[31mPara parar digite 999\33[m')

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n    
print('A soma dos \33[32m{}\33[m valores foi \33[32m{}\33[m'.format(c, s))