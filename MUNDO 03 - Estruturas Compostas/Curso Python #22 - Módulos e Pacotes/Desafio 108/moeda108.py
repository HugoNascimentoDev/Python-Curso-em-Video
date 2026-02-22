# Funções

def aumentar(n, taxa = 0):
    valor = n * (1 + taxa)
    return valor
    
    
def diminuir(n, taxa = 0): 
    valor = n * (1 - taxa)
    return valor

    
def dobro(n):
    valor = n * 2
    return valor

    
def metade(n):
    valor = n / 2
    return valor


def moeda(n = 0, moeda = "R$ "):
    if moeda == 'R$ ':
        valor = f'{moeda}{n:.2f}'.replace('.',',')
    else:
        valor = f'{moeda}{n:.2f}'
    return valor