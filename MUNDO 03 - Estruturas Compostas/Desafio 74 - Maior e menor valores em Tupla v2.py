# # Arquivo Desafio 74.py
# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = []
contador = 0
maior = menor = 0

while contador < 5:
    num = randint(1,10)
    numeros.append(num)
    if contador == 0:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    contador += 1
print(f'Tupla: {tuple(numeros)}')
print(f'O MAIOR número é o {maior}')
print(f'O MENOR número é o {menor}')