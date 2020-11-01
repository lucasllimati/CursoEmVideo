# 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Valor \33[31m{}\33[m inválido! Por favor, informe o seu sexo: '.format(sexo)))

print('O sexo {} foi registrado com sucesso!'.format(sexo))
print('n\FIM!')