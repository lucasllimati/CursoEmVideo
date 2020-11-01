# EXERCÍCIO 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

#strip - remove espaços desnecessários
nome = str(input('Digite o seu nome completo: ')).strip()
pnome = nome.split()

print('Nome completo: {}'.format(nome).title())
print('Nome nome em maiúsculo é: {}'.format(nome.upper()))
print('Nome nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome completo possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e possui {} letras'.format(pnome[0].upper(), len(pnome[0])))

