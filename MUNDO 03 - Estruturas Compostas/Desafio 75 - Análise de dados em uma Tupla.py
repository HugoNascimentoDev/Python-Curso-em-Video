# # Arquivo Desafio 75.py
# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')),int(input('Digite um número: ')))

# A) Quantas vezes apareceu o valor 9.
if 9 in numeros:
    print(f'O número 9 apareceu {numeros.count(9)}x na tupla.')
else:
    print(f'O número 9 não foi encontrado na tupla.')

# B) Em que posição foi digitado o primeiro valor 3.
if 3 in numeros:
    posicao_num_tres = numeros.index(3)
    print(f'O primeiro número três foi encontrado na {posicao_num_tres}ª posição.')
else:
    print(f'O número 3 não foi encontrado na tupla.')

# C) Quais foram os números pares.

contador = 0
for n in numeros:
    if n % 2 == 0:
        print(f'o número {n} é PAR!')
        contador += 1
print(f'Foram encontrados {contador} números pares.')