# Arquivo Desafio 107.py
# Seu código aqui
# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

n = float(input('Digite um valor: '))

print(f'O valor R$ {n:.2f} com o aumento de 10% é igual a R$ {moeda.aumentar(n, 0.10):.2f}.')
print(f'O valor R$ {n:.2f} com o desconto de 10% é igual a R$ {moeda.diminuir(n, 0.10):.2f}.')
print(f'O dobro do valor R$ {n:.2f} é igual a {moeda.dobro(n):.2f}.')
print(f'A metade do valor R$ {n:.2f} é igual a {moeda.metade(n):.2f}.')