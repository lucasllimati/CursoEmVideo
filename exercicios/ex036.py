# EXERCÍCIO 36
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento: '))

prestacao = valorcasa / (tempo * 12)
minpretacao = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} e {} anos a prestação será de R${:.2f}.'.format(valorcasa, tempo, prestacao))
if prestacao <= minpretacao:
    print('Empréstimo foi \033[32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[31mNEGADO\033[m!') 