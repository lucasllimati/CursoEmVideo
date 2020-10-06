# 59
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

opc = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while opc != 8:
    print('''
        [1] - SOMAR
        [2] - SUBTRAIR
        [3] - MULTIPLICAR
        [4] - DIVIDIR
        [5] - MAIOR
        [6] - MENOR
        [7] - NOVOS NÚMEROS
        [8] - SAIR DO PROGRAMA
    ''')
    opc = int(input('Qual é a sua opção? '))
    
    if opc == 1:
        print('A soma entre {} + {} é {}'.format(num1, num2, num1 + num2))
    if opc == 2:
        print('A subtração entre {} + {} é {}'.format(num1, num2, num1 - num2))
    if opc == 3:
        print('A multiplicação entre {} + {} é {}'.format(num1, num2, num1 * num2))
    if opc == 4:
        print('A divisão entre {} + {} é {:.2f}'.format(num1, num2, num1 / num2))
    if opc == 5:
        if num1 >= num2:
            maior = num1
        else:
            maior = num2
        print('O maior valor entre {} + {} é {:.2f}'.format(num1, num2, maior))
    if opc == 6:
        if num1 <= num2:
            menor = num1
        else:
            menor = num2
        print('O menor valor entre {} + {} é {:.2f}'.format(num1, num2, menor))
    if opc == 7:
        print('ALTERAR VALORES...')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    if opc == 8:
        print('Finalizando...')
    
    print('=-' * 10)

print('Fim do programa! Volte sempre')
