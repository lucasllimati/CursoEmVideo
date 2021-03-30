def leiaInt(msg):
    """
    -> Valida valores do tipo inteiro.
    :param msg: Mensagem que será exibida para entrada do valro inteiro
    :return: Valor inteiro
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam = 35):
    """
    -> Retorna uma linha.
    :param tam: quantidade de dashes que a linha terá
    :return: linha
    """
    return '-' * tam

def cabecalho(txt):
    """
    -> Cria um texto centralizado com linhas acima e abaixo.
    :param txt: Texto que será exibido entre as linhas
    :return: Sem retorno
    """
    print(linha())
    print(txt.center(35))
    print(linha())

def menu(lista):
    """
    -> Faz um menu com as opções passadas e retorna a opção que usuário escolher.
    :param lista: opções que serão colocadas no menu.
    :return: opção escolhida pelo usuário.
    """
    cabecalho('\033[34mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc