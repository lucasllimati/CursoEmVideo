# EXERCÍCIO 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 20)
print('Analisador de Triângulo')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('Os segmentos ({} - {} - {}) PODEM FORMAR um triângulo!'.format(a, b, c))
else:
    print('Os segmentos ({} - {} - {}) NÃO PODEM FORMAR um triângulo!'.format(a, b, c))

#OUTRA FORMA
'''if a < b + c and b < a + c and c < a + b
    print('Os segmentos ({} - {} - {}) PODEM FORMAR um triângulo!'.format(a, b, c))
else:
    print('Os segmentos ({} - {} - {}) NÃO PODEM FORMAR um triângulo!'.format(a, b, c))'''