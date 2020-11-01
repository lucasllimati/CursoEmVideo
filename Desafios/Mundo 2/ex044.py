# EXERCÍCIO 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal 
# 3x ou mais no cartão: 20% de juros

print('=' * 10,end=' ')
print('\33[36mLOJAS LIMA\33[m',end=' ')
print('=' * 10)
preco = float(input('Digite o preço das compras: R$'))
print('\33[32mFORMAS DE PAGAMENTO\33[m')
print('[ 1 ] - à vista dinheiro/cheque')
print('[ 2 ] - à vista no cartão')
print('[ 3 ] - 2x no cartão')
print('[ 4 ] - 3x ou mais no cartão')
opc = int(input('Digite uma opção: '))

if opc == 1: # à vista dinheiro/cheque: 10% de desconto
    total = preco - (preco * 10 / 100)
    print('Sua compra de \33[32mR${:.2f}\33[m vai custar \33[32mR${:.2f}\33[m no final.'.format(preco, total))

elif opc == 2: # à vista no cartão: 5% de desconto
    total = preco
    print('Sua compra vai custar \33[32mR${:.2f}\33[m.'.format(preco))

elif opc == 3: # em até 2x no cartão: preço normal 
    parcela = int(input('Quantas parcelas: '))    
    valorparcela = preco / parcela
    print('Sua compra será parcelada em \33[32m{}x\33[m de \33[32mR${:.2f}\33[m SEM JUROS.'.format(parcela, valorparcela),end=' ')
    print('Sua compra vai custar \33[32mR${:.2f}\33[m.'.format(preco))

elif opc == 4:# 3x ou mais no cartão: 20% de juros
    parcela = int(input('Quantas parcelas: '))    
    total = preco + (preco * 20 / 100)
    valorparcela = total / parcela
    print('Sua compra será parcelada em \33[32m{}x\33[m de \33[32mR${:.2f}\33[m COM JUROS.'.format(parcela, valorparcela),end=' ')
    print('Sua compra de \33[32mR${:.2f}\33[m vai custar \33[32mR${:.2f}\33[m no final.'.format(preco, total))

else:
    print('\33[31mOpção inválida!\33[m')

