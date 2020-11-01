# 67
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

# Description
# n ~> number entered
# c ~> counter

print('-=-' * 15)
print('\t\tTABUADA')
print('-=-' * 15)

while True:
    n = int(input('Digite um número: '))
    c = 0
    if n < 0:
        break
    # Using the 'while' loop
    while c <= 10:
        print('{} x {} = {}'.format(n, c, n * c))
        c += 1
    print('')
    # Using the 'for' loop
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('')
print('\n\n')
print('~'*25)
print('\33[31mFIM\33[m')
print('~'*25)