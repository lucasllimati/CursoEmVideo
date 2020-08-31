# EXERCÍCIO 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('-=-' * 20)
print('\t\tAnalisador de Triângulo')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('Os segmentos ({} - {} - {}) \33[36mPODEM FORMAR\33[m um triângulo'.format(a, b, c),end =' ')
    if a == b == c:
        print('\33[36mEQUILÁTERO\33[m -> todos os lados iguais')
    elif a == b != c or a == c != b or b == c != a:
        print('\33[36mISÓSCELES\33[m -> dois lados iguais, um diferente')
    else:
        print('\33[36mESCALENO\33[m -> todos os lados diferentes')
else:
    print('Os segmentos ({} - {} - {}) NÃO PODEM FORMAR um triângulo!'.format(a, b, c))