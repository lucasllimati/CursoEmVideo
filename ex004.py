# EXERCÍCIO 4
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações 
# possíveis sobre ele.
valor = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}'.format(type(valor)))
print('Só tem espeça? {}'.format(valor.isspace()))
print('É um número? {}'.format(valor.isnumeric()))
print('É alfabético? {}'.format(valor.isalpha()))
print('É alfanumérico? {}'.format(valor.isalnum()))
print('Está em maiúsculo? {}'.format(valor.isupper()))
print('Está em munúculo? {}'.format(valor.islower()))
print('Está capitalizado? {}'.format(valor.istitle()))