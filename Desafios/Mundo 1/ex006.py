# EXERCÍCIO 6
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
#rq = n ** (1/2)
rq = pow(n, (1/2))

print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'. format(n, t))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, rq))
