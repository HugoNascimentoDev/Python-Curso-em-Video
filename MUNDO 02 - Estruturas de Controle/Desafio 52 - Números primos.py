# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

c_primo = 0
for n in range (1, num + 1):
    if num % n == 0:
        c_primo += 1

if c_primo != 0 and c_primo == 2:
    primo = 'É PRIMO'
else:
    primo = 'NÃO É PRIMO'

print(f'O número {num} foi divisível {c_primo} vezes.')
print(f'E por isso ele {primo}!')
