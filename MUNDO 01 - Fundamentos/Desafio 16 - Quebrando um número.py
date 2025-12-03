# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input("Digite um valor real: "))
print(f'''Número Digitado: {num}
Porção inteira {math.trunc(num)}''')
