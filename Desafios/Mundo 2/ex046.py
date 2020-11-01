# EXERCÍCIO 46
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
num = 10
for cont in range(0, 11):
    print(num)
    num = num - 1
    sleep(0.2)    
print('BUM! BUM! POOOW! ')

#OUTRA FORMA
'''
for cont in range(10, -1, -1):
    print(num)
    num = num - 1
    sleep(0.2)    
print('BUM! BUM! POOOW! ')'''
