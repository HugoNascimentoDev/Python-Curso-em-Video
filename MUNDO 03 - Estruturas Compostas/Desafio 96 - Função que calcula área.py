# Arquivo Desafio 96.py
# Seu código aqui
# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def linha():
    print('-'*50)

def area(l, c):
    a = l * c
    linha()
    print(f'A área de um terrono {l:.2f} x {c:.2f} (largura x comprimento) é de {a:.2f} m².')
    linha()

linha()
print(f'{'CONTROLE DE TERRENOS':^50}')
linha()
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(l, c)
