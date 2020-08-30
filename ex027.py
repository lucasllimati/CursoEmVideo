# EXERCÍCIO 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).upper().strip()
nomesep = nome.split()

print('Prazer em te conheecer!')
print('Seu primeiro nome é: {}'.format(nomesep[0]))
print('Seu último nome é: {}'.format(nomesep[-1]))

#Outra forma
#print('Seu último nome é: {}'.format(len(nomesep[len(nome)-1]))
