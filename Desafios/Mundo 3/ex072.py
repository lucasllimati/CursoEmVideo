# 72
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Description
# numero ~> tuple with the values ​​(1 - 20) in full
# num ~> number entered by the user

numero = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')

while True:
    num = int(input('Digite um número entre 0 e 20: ')) 
    # if num < 0 or num > 20: # Complete condition
    if 0 < num > 20: # Abbreviated condition
        print('\33[31mTente novamente\33[m.')
    else:
        print(f'\nVocê digitou o número \33[32m{numero[num]}\33[m')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nQuer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('\n\n{:=^30}'.format('PROGRAMA FINALIZADO...'))