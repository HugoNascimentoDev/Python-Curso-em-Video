# # Arquivo Desafio 85.py
# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for n in range(7):
    num = int(input(f'{n + 1}º Valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('='*40)
print(f'Todos os valores: {numeros}')
print('='*40)
print(f'Os valores PARES digitados foram: {sorted(numeros[0])}')
print(f'Os valores ÍMPARES digitados foram: {sorted(numeros[1])}')
print('='*40)

