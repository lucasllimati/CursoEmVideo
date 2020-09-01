# EXERCÍCIO 49
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-=-' * 10, end=' ')
print('TABUADA', end=' ')
print('-=-' * 10)

num = int(input('Digite um número oara ver sua tabuada: '))

for i in range (0, 11):
    print('{} x {} = {}'.format(i, num, i * num))
print('\n\nFIM')