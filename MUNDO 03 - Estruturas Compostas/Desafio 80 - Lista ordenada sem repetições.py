# # Arquivo Desafio 80.py
# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for n in range (5):
    num = int(input(f'Digite o {n+1}º valor: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                break
            posicao += 1

print('=' * 40)
print(f'Lista final ordenada: {lista}')
print('=' * 40)