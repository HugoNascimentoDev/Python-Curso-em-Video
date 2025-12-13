# # Arquivo Desafio 81.py
# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
numeros = []
c = 0
while True:
    num = int(input(f'Digite o {c + 1}º número: '))
    numeros.append(num)
    c += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0  ]
    if resp == 'N':
        break

print('Os números digitados foram: ', end = ' ')
for n in numeros:
    print(f'{n}', end = ' ')
# A) Quantos números foram digitados.
print(f'\nForam digitados: {len(numeros)} números.')

# B) A lista de valores, ordenada de forma decrescente.
print(f'A lista em ordem CRESCENTE: {sorted(numeros)}')

print(f'A lista em ordem DECRESCENTE: {sorted(numeros, reverse= True)}')

# C) Se o valor 5 foi digitado e está ou não na lista.

if 5 in numeros:
    print(f'O número 5 foi digitado {numeros.count(5)} vezes.')
else:
    print(f'O número 5 não foi encontrado na lista!')




