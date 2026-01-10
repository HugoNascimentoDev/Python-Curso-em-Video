# # Arquivo Desafio 91.py
# # Seu código aqui
# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {}

for jogador in range(1, 5):
    jogadas[f'{jogador}º JOGADOR'] = randint(1,6)

print('=' * 20)  
print(f'{"JOGADAS":^20}')
print('=' * 20)  

for k, v in jogadas.items():
    print(f'{k} = {v}')
    sleep(0.5)

print('=' * 20) 
print(f'{"EM ORDEM":^20}')
print('=' * 20) 

ranking = []

ranking = sorted(jogadas.items(), key= itemgetter(1), reverse = True)

for i, n in enumerate(ranking):
    print(f'{i + 1}º Lugar = {n[0]} com a jogada {n[1]} no dado.')
    sleep(0.5)

print('=' * 20) 
