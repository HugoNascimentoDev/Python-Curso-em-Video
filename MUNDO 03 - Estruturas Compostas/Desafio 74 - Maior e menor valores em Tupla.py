# # Arquivo Desafio 74.py
# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'TUPLA criada: {numeros}')
print(f'MAIOR valor: {max(numeros)}')
print(f'MENOR valor: {min(numeros)}')