# EXERCÍCIO 37
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('Selecione uma das bases para conversão: ')
print('\t[ 1 ] - Binário\n\t[ 2 ] - Octal\n\t[ 3 ] - Hexadecimal')

opc = int(input('Sua opção: '))

if opc == 1:
    print('\33[34m{}\33[m convertido para \33[34mBINÁRIO\33[m é igual a \33[34m{}\33[m.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('\33[34m{}\33[m convertido para \33[34mOCTAL\33[m é igual a \33[34m{}\33[m.'.format(num, oct(num)[2:]))
elif opc == 3:
    print('\33[34m{}\33[m convertido para \33[34mHEXADECIMAL\33[m é igual a \33[34m{}\33[m.'.format(num, hex(num)[2:]))
else:
    print('\33[31m Opção inválida!Tente novamente.\33[m')
