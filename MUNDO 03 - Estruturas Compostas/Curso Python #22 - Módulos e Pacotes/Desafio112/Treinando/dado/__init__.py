#função

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;031m<<< ERRO >>> "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


