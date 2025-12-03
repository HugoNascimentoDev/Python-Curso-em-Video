# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8


print('=' * 38)
print('\tSEQUÊNCIA DE FIBONACCI')
print('=' * 38)
num = int(input('Quantos termos quer mostrar? '))

t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end= '')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end= '')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')