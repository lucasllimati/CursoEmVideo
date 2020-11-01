# EXERCÍCIO 24
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

nome = str(input('Digite o nome da cidade: ')).upper().strip()
print('Começa com a palavra SANTO: {}'.format(nome[:5] == 'SANTO'))

#MELHORIA - VERIFICA SE POSSUI SANTO NA FRASE INTEIRA
print('Possui SANTO no nome: {}'.format('SANTO' in nome))