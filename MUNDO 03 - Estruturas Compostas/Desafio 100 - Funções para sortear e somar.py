# Arquivo Desafio 100.py
# Seu código aqui

# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteia(n):
    numeros.clear()
    print('=' * 50)
    print('Sorteando valores...')
    print('-' * 50)
    for c in range(n):
        num = randint(0,10)
        numeros.append(num)
        print(f'{num}', end = ' ', flush = True)
        sleep(0.5)
    
    
def somaPar():
    print('=' * 50)
    print('Analisando valores...')
    print('-' * 50)
    sleep(0.5)
    soma = 0
    contador = 0
    pares = []
    for n in numeros:
        if n % 2 == 0:
            soma += n
            contador += 1
            pares.append(n)
    print(f'Na lista {numeros}.\nOs valores {pares} são pares!\nContamos {contador} número(s) par(es) e a soma destes valores é igual a {soma}!')
    print('=' * 50)


sorteia(10)
print()
somaPar()
