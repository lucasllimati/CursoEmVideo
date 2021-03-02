# 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: – Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional).

def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param n: um ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao.
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    resultado = dict()
    resultado['total'] = len(n) 
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    resultado['média'] = sum(n) / len(n)
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'BOA'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'RAZOÁVEL'
        else:
            resultado['situação'] = 'RUIM'
    return resultado

# Programa principal
resp = notas(5.5, 7.5, 10, 9.5, sit=True)
print(resp)
help(notas)