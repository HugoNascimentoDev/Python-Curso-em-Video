# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
n3 = int(input('Digite o 3º valor: '))

# Verificando o maior valor
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificando o menor valor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

print(f'{maior} é o MAIOR número!')
print(f'{menor} é o MENOR número!')