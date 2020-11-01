# EXERCÍCIO 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
idadevelho = 0
totalmulher20 = 0
nomevelho = ''

for i in range (1,5):
    print('----- {}ª pessoa -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if i == 1 and sexo in 'Mm' or sexo in 'Mm' and idade > idadevelho :
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Fm' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O nome do homem mais velho tem {} anos e se chama {}.'.format(idadevelho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalmulher20))



