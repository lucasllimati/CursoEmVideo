# EXERCÍCIO 40
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média 7.0 ou superior: APROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média abaixo de 5.0: REPROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('Tirando {} e {}, a média do aluno é {}.'.format(nota1, nota2, media))
if media <= 7.0:
    print('O aluno está \33[36mAPROVADO\033[m')
elif media >= 5.0 and media >= 6.9:
    print('O aluno está de \33[33mRECUPERAÇÃO\033[m.')
else:
    print('O aluno está \33[31mREPROVADO\033[m.')