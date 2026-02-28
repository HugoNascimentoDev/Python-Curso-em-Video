# Arquivo Desafio 115.py
# Seu código aqui

# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

from Lib.Interface import *
from Lib.Arquivo import *
from time import sleep

arquivo = 'Road_to_dev_2026.txt'

if not ArquivoExiste(arquivo):
    CriarArquivo(arquivo)

cabecalho('Road to Dev 2026')

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    sleep(1)
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        cabecalho('CADASTROS')
        LerArquivo(arquivo)
        sleep(1)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Digite o nome: ').upper().strip()
        idade = leiaInt('Digite a idade: ')
        NovoCadastro(arquivo, nome, idade)
        sleep(1)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!!!')
        break
    else:
        print(erro('<<< ERRO >>> Digite uma opção válida!'))
