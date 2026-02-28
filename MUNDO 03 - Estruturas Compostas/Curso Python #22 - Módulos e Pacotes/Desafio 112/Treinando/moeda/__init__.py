# Funções

def aumentar(n, taxa = 0, formatado = False):
    valor = n * (1 + taxa)
    return valor if not formatado else moeda(valor)
    
    
def diminuir(n, taxa = 0, formatado = False): 
    valor = n * (1 - taxa)
    return valor if not formatado else moeda(valor)

    
def dobro(n, formatado = False):
    valor = n * 2
    return valor if not formatado else moeda(valor)

    
def metade(n, formatado = False):
    valor = n / 2
    return valor if not formatado else moeda(valor)


def moeda(n, moeda = "R$"):
    return f'{moeda} {n:>.2f}'.replace('.', ',')

def resumo (n, taxaa = 0.05, taxad = 0.05):
    print('=' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('=' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaa:.2%} de aumento: \t{aumentar(n, taxaa, True)}')
    print(f'{taxad:.2%} de redução: \t{diminuir(n, taxad, True)}')
    print('-' * 35)
