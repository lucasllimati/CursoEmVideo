# 77
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Description

palavras = (
    'aprender',
    'programar',
    'linguagem',
    'python',
    'curso',
    'gratis',
    'estudar',
    'praticar',
    'trabalhar',
    'mercado',
    'programador',
    'futuro'
)

for p in palavras:
    print(f'\nNa palavra \33[32m{p.upper()}\33[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\33[32m{letra.upper()}\33[m', end=' ')
