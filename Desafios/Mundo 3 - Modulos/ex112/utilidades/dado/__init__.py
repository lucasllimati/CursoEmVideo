def leiaDinheiro(msg):
    '''
    -> Funcao: validacao da mensagem/input
    '''
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == "":
            print(f'\033[0;31mErro! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)