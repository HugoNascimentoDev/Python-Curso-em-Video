def erro(msg):
    return f'\033[31m {msg} \033[m'


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(erro(f'<<< ERRO >>> Digite um número inteiro válido! '))
            continue
        except (KeyboardInterrupt):
            print(erro(f'<<< ERRO >>> Entrada de dados interrompida!'))
            return 0
        else:
            return n
       


def linha (tamanho = 50):
    return '-' * tamanho


def cabecalho (texto):
    print(linha())
    print(texto.center(50).upper())
    print(linha())


def menu (lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for c in lista:
        print(f'\033[33m{contador}\033[m - \033[36m{c.upper()}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao

    