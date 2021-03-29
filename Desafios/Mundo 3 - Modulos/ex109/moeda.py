# Moeda
# 109
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preco = 0, taxa = 0, formato = False):
    '''
    -> Funcao: calcula o aumento do preco.
    :param preco: valor a ser calculado
    :param taxa: valor (percentual) do aumento
    :param formato: Caso a opcao seje 'True' ele ira formatar o resultado, por padrao esta false, ou seja, o resoltado nao ser formatado.
    :return: resultado da operacao
    '''
    res = preco + (preco * taxa / 100)
    return res if formato is False else moedaFormat(res)
    # return res if not formato else moedaFormat(res)

def diminuir(preco = 0, taxa = 0, formato = False):
    '''
    -> Funcao: calcula o desconto/dimunuicao do preco.
    :param preco: valor a ser calculado
    :param taxa: valor (percentual) do desconto/dimunuicao
    :param formato: Caso a opcao seje 'True' ele ira formatar o resultado, por padrao esta false, ou seja, o resoltado nao ser formatado.
    :return: resultado da operacao
    '''
    res =  preco - (preco * taxa / 100)
    return res if formato is False else moedaFormat(res)

def dobro(preco = 0, formato = False):
    '''
    -> Funcao: calcula o dobro preco.
    :param preco: valor a ser calculado
    :param formato: Caso a opcao seje 'True' ele ira formatar o resultado, por padrao esta false, ou seja, o resoltado nao ser formatado.
    :return: resultado da operacao
    '''
    res =  preco * 2
    return res if formato is False else moedaFormat(res)    

def metade(preco = 0, formato = False):
    '''
    -> Funcao: calcula a metade preco.
    :param preco: valor a ser calculado
    :param formato: Caso a opcao seje 'True' ele ira formatar o resultado, por padrao esta false, ou seja, o resoltado nao ser formatado.
    :return: resultado da operacao
    '''
    res =  preco / 2
    return res if formato is False else moedaFormat(res)

def moedaFormat(preco = 0, moeda = 'R$'):
    return f'\33[32m{moeda} {preco:.2f}\33[m'.replace('.' ,',')

def taxaFormat(taxa = 0, porcentagem = '%'):
    return f'\33[32m{taxa:.2f} {porcentagem}\33[m'.replace('.' ,',')