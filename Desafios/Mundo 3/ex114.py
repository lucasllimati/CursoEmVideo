# 114
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from time import sleep
import urllib
import urllib.request
import webbrowser

try:
    # site = urllib.request.urlopen("www.pudim.com.br")
    urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento. Deu erro!\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso. Tudo OK!\033[m')
    print('Abrindo o site...')
    sleep(2)
    webbrowser.open('http://www.pudim.com.br', new = 2)