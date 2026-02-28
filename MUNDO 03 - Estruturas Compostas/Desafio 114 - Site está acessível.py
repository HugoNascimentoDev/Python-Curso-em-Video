# Arquivo Desafio 114
# .py
# Seu código aqui

# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site Indisponível!')
else:
    print('Site disponível!')