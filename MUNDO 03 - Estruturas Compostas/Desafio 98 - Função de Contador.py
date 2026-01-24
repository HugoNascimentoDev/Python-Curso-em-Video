# Arquivo Desafio 98.py
# Seu código aqui

# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def linha(simbolo):
    print(simbolo * 60) 

def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    linha('=')
    print(f'Contagem de {inicio} até {fim}, contado de {passo} em {passo}.')
    linha('-')

    if inicio < fim:
        for n in range (inicio, fim + 1, passo):
            print(n, end= ' ', flush= True)
            sleep(0.5)
        print('<<< FIM >>>')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ', flush= True)
            sleep(0.5)
            cont -= passo
        print('<<< FIM >>>')
    


contador(1, 10, 1)
contador(20, 0, 2)

print('Crie sua contagem personalizada!!!')

i = int(input('Digite o INICIO: '))
f = int(input('Digite o FIM: ')) 
p = int(input('Digite o PASSO: '))

contador(i, f, p)



