# Arquivo Desafio 99.py
# Seu código aqui

# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def linha (simbol):
    print(f'{simbol}' * 60)

def maior(*args):
    print('Analisando valores...', flush = True)
    sleep(0.5)
    tamanho = len(args)
    maior = max(args)
    for n in args:
        print(f'{n}', end = ' ', flush= True)
        sleep (0.5)
    sleep(0.5)
    print(f'\nForam analisados o TOTAL de {tamanho} números e o MAIOR número é o {maior}!')
    linha('=')


maior(5, 7, 8, 10)

maior(5, 7, 8, 9, 10, 11, 13, 20, 50)
        


