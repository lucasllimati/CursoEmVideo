# 63
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-'*25)
print('\33[32mSequência de Fibonacci\33[m')
print('-'*25)

n = int(input('Quantos termos você quer mostrar? '))
termo = 0
prox = 1
c = 0

while c < n:
    print('{}'.format(termo), end=' → ')
    aux = termo + prox
    termo = prox 
    prox = aux      
    c += 1
print('\33[31mFIM\33[m')
print('~'*25)
