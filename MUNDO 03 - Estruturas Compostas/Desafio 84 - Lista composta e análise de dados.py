# # Arquivo Desafio 84.py
# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
pesado = leve = 0

while True:
    dados.append(input('Digite seu nome: '))
    dados.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').upper().strip()[0]
    if resp == 'N':
        break
print('='*60)
print(pessoas)
print('='*60)
# A) Quantas pessoas foram cadastradas.
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')

# B) Uma listagem com as pessoas mais pesadas.
print(f'O MAIOR peso foi de {pesado:.2f} KGs. Pessoas mais pesadas:', end = ' ')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')

# C) Uma listagem com as pessoas mais leves.
print(f'\nO MENOR peso foi de {leve:.2f} KGs. Pessoas mais leves:', end = ' ')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}]', end= ' ')
print('='*60)