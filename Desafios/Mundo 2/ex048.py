# EXERCÍCIO 48
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

cont = 0
soma = 0

for num in range (1,501):
    if num % 2 == 1 and num % 3 == 0:
        soma += num
        cont += 1
        print(num, end=' ')
print('\n\nA soma de todos os {} valores solicitados é {}.'.format(cont, soma))

#OUTRA FORMA
'''
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1'''
    
