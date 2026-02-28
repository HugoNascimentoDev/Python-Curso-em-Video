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


def formatando_moeda(n, escolha_moeda = '1', formatar = True):
    if formatar == True:
        valor = n
        if escolha_moeda == '1':
            valor = f'R$ {n:.2f}'.replace('.',',')
        elif escolha_moeda == '2':
            valor = f'$ {n:.2f}'
    else:
        valor = n
        
    return valor