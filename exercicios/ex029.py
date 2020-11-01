# EXERCÍCIO 29
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual é sua velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    print('Você deve pagar uma multa no valor de R$ {:.2f}!'.format(multa))    
print('Tenha um bom dia! Dirija com segurança!')