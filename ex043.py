# EXERCÍCIO 43
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (M): '))
imc = peso / pow(altura, 2)

print('O IMC desssa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está \33[31mABAIXO DO PESO\33[m normal!')
elif imc <= 25:
    print('PARABÉNS,você está na faixa de \33[32mPESO NORMAL\33[m!')
elif imc <= 30:
    print('Você está em \33[31mSOBREPESO\33[m!')
elif imc <= 40:
    print('Você está em \33[31mOBESIDADE\33[m!')
else:
    print('Você está em \33[31mOBESIDADE MÓRBIDA\33[m!')