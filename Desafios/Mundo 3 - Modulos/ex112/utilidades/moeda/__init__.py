# Moeda
# 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

def aumentar(preco = 0, taxa = 0, formato = False):
    '''
    -> Funcao para calcular o aumento do preco.
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
    -> Funcao para calcular o desconto/dimunuicao do preco.
    :param preco: valor a ser calculado
    :param taxa: valor (percentual) do desconto/dimunuicao
    :param formato: Caso a opcao seje 'True' ele ira formatar o resultado, por padrao esta false, ou seja, o resoltado nao ser formatado.
    :return: resultado da operacao
    '''
    res =  preco - (preco * taxa / 100)
    return res if formato is False else moedaFormat(res)

def dobro(preco = 0, formato = False):
    '''
    -> Funcao para calcular o dobro preco.
    :param preco: valor a ser calculado
    :param formato: Caso a opcao seje 'True' ele ira formatar o resultado, por padrao esta false, ou seja, o resoltado nao ser formatado.
    :return: resultado da operacao
    '''
    res =  preco * 2
    return res if formato is False else moedaFormat(res)    

def metade(preco = 0, formato = False):
    '''
    -> Funcao para calcular a metade preco.
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

def resumo(preco = 0, taxaAumento = 10, taxaReducao = 5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moedaFormat(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaFormat(taxaAumento)} de aumento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'{taxaFormat(taxaReducao)} de redução: \t{diminuir(preco, taxaReducao, True)}')
    print('-' * 35)
