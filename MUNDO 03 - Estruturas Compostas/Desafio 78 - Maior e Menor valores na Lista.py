# Arquivo Desafio 78.py
# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lista_numeros = []
print(lista_numeros)
for n in range(5):
    num = int(input(f'Digite {n + 1}º número: '))
    lista_numeros.append(num)

print(lista_numeros)
print(f'O MAIOR número é igual {max(lista_numeros)} sua posição na lista é {lista_numeros.index(max(lista_numeros)) + 1}ª.')
print(f'O MENOR número é igual {min(lista_numeros)} sua posição na lista é {lista_numeros.index(min(lista_numeros)) + 1}ª.')