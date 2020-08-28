# EXERCÍCIO 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

 '''
CONSIDERE A COTAÇÃO ABAIXO -> MOEDA REAL BR SENDO COMPARADA COM AS DEMAIS MOEDAS 
DATA: 27/08/2020
LINK: https://www.bcb.gov.br/conversao
DÓLAR EUA = R$ 0.1787118
EURO = € 0.1511168
DÓLAR CANADENSE = C$ 0.2343073
DÓLAR DA NOVA ZELÂNDIA = NZ$ 0.2690631
DÓLAR AUSTRALIANO = A$ 0.2461236'''

dinheiro = float(input('Quando dinheiro você tem na carteira? R$ '))
dolareua = dinheiro * 0.1787118
euro = dinheiro * 0.1511168
dcanadense = dinheiro * 0.2343073
dnovazelandia = dinheiro * 0.2690631
daustraliano = dinheiro * 0.2461236

print('Com R$ {} você pode comprar U$ {:.2f}'.format(dinheiro, dolareua))
print('Com R$ {} você pode comprar U$ {:.2f}'.format(dinheiro, euro))
print('Com R$ {} você pode comprar C$ {:.2f}'.format(dinheiro, dcanadense))
print('Com R$ {} você pode comprar NZ$ {:.2f}'.format(dinheiro, dnovazelandia))
print('Com R$ {} você pode comprar A$ {:.2f}'.format(dinheiro, daustraliano))
