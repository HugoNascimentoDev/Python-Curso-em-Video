# Arquivo Desafio 106.py
# Seu código aqui

# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

# criando uma lista com as informações de cores

cores = ('\033[m',          # 0 - SEM cores
        '\033[0;30;41m',    # 1 - Vermelho
        '\033[0;30;42m',    # 2 - Verde
        '\033[0;30;43m',    # 3 - Amarelo
        '\033[0;30;44m',    # 4 - Azul
        '\033[0;30;45m',    # 5 - Roxo
        '\033[7;30m',       # 6 - Branco
         )

def titulo (msg, cor = 0):
    tam = len(msg)
    print(cores[cor])
    print('~' * (tam + 4))
    print(f'  {msg}')
    print('~' * (tam + 4))
    print(cores[0])

def volte_sempre (msg2):
    tam_volte = len(msg2)
    print('~' * (tam_volte + 4))
    print(f'  {msg2}')
    print('~' * (tam_volte + 4))   

def ajuda(comand):
    help(comand)



comando = ''
while True:
    titulo('AJUDA INTERATIVA pyHELP', 1)
    comando = input('Função, biblioteca ou FIM para finalizar --> ')
    if comando.upper().strip() == 'FIM':
        volte_sempre('<<<<< VOLTE SEMPRE!!! >>>>>')
        break
    else:
        ajuda(comando)
