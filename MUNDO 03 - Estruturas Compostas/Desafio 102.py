# Arquivo Desafio 102.py
# Seu código aqui

# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial (n = 0, show = False):
    """-> Calcula o Fatorial de um número: 
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end = '')
            else:
                print(f'{c} = ', end = '')
        f *= c

    return f

print(fatorial(4, show = True))