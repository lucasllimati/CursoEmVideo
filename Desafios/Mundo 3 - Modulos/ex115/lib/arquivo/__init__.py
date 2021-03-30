from lib.interface import *

def arquivoExiste(nome):
    """
    -> Verifica se existe um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo
    :return: True se existe, False se não existe.
    """
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    """
    -> Cria um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo de texto
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    """
    -> Lê o conteúdo de um arquivo de texto.
    :param nome: Nome do arquivo de texto.
    :return: Sem retorno.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(sep=';')  # Separa a linha por ponto e vírgula.
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    """
    -> Insere o nome e idade de uma pessoa em um arquivo de texto.
    :param arq: Nome do arquivo em que será salvo os dados.
    :param nome: (opcional) Nome da pessoa que será salvo.
    :param idade: (opcional) Idade da pessoa que será salvo.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'at', encoding='utf-8')
    except:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao cadastrar os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
