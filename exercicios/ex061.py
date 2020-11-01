# 61
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('\33[32mGerador de PA\33[m')
print('=+'*10)

# Description
# p = first term
# r = reason
# t = term
# c = counter

p = int(input('Primeiro termpo: '))
r = int(input('Razão da PA: '))
t = p
c = 1

while c <= 10:
    print('{}'.format(t), end=' → ')
    t += r
    c += 1
print('\33[31mFIM\33[m')