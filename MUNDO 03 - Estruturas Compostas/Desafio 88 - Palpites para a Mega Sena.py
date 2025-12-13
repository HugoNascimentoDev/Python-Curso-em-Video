# # Arquivo Desafio 88.py
# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep
palpites = []

jogos = int(input('Quantos jogos deseja fazer? '))
print('='*40)
print(f'{"LISTA DE JOGOS":^40}')
print('='*40)
for n in range (0, jogos):
    palpites.append(sorted(sample(range(1,61), 6)))
      
for i, jogo in enumerate(palpites, start= 1):
    print(f'{i}º Jogo: {jogo}')
    sleep(0.5)
print('='*40)

print(f'Todos os jogos: {palpites}')


    

