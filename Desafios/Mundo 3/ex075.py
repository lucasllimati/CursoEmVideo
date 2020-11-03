# 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

# Description

num = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)

print(f'Você digitou os valores \33[36m{num}\33[m')
print(f'O valor 9 apareceu \33[36m{num.count(9)}\33[m')
if 3 in num:
    print(f'O valor 3 apareceu na \33[36m{num.index(3)+1}\33[mª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(f'\33[36m{n}\33[m', end=' ')
print('\n\n')

