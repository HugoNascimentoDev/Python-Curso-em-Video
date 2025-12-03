# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

import time

nome = input('Digite seu nome completo: ')
print('Analisando seu nome: ')
time.sleep(1.5)
# O nome com todas as letras maiúsculas e minúsculas.
print(f'Maiúscula: {nome.upper()}')
time.sleep(1.5)
print(f'Minúsculas: {nome.lower()}')
time.sleep(1.5)
print(f'Apenas primeiras letras em Maiúsculas: {nome.title()}')

# Quantas letras ao todo (sem considerar espaços).
nome_sem_espaço = nome.replace(' ', '')
time.sleep(1.5)
print(f'Total de letras: {len(nome_sem_espaço)}')

# Quantas letras tem o primeiro nome.

separa = nome.split()
print(f'Seu primeiro nome é {separa[0].upper()} e ele tem {len(separa[0])} letras.')




