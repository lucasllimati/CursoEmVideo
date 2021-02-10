# 96
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno de \33[36m{larg}\33[m x \33[36m{comp}\33[m é de \33[36m{area}\33[m m²')


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m):'))
area(largura, comprimento)