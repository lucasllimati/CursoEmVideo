# 71
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 35)
print('\t\tBANCO LLL')
print('=' * 35)

valor = int(input('Que valor você quer sacar? R$ '))

#1 - forma
while True:    
    if valor >= 50:
        nota50 = valor // 50
        resto = valor % 50
        print(f'Total de \33[32m{nota50}\33[m  cédulas de R$ 50') 
    if resto >= 20:
        nota20  = resto // 20
        resto = valor % 20
        print(f'Total de \33[32m{nota20}\33[m  cédulas de R$ 20') 
    if resto >= 10:
        nota10  = resto // 10
        resto = valor % 10
        print(f'Total de \33[32m{nota10}\33[m  cédulas de R$ 10') 
    if resto > 0:
        moeda1  = resto // 1
        resto = valor % 1
        print(f'Total de \33[32m{moeda1}\33[m moedas de R$ 1')
    break

# #2 - forma
# total = valor
# ced = 50
# totalced = 0

# while True:    
#     if total >= ced:
#         total -= ced
#         totalcel += 1
#     else:
#         if totalcel > 0:
#             print(f'Total de {totalced} cédulas de R$ {ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         if total = 0:
#             break
print('=' * 35)
print('Volte sempre ao BANCO LLL! Tenha um bom dia.')