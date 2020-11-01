# 65
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# Description
# continuar ~> user response 'do you want to continue?' / validation
# cont ~> counter
# soma ~> sum
# maior ~> highest value / max
# menor ~> lower value / min
# media ~> average / avg

continuar = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
media = 0
# cont = soma = maior = menor = media = 0

while continuar in 'Ss':
    num = int(input('Digite um número: '))   
    soma += num
    cont += 1
    if cont == 1:        
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    continuar = input('Quer continuar? [S/N]   ').upper().split()[0]
media = soma / cont
print('Você digitou {} número e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))