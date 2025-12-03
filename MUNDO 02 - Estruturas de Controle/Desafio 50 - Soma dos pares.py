# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


s = 0
c_pares = 0
for n in range(1, 7):
    valor = int(input(f'Digite o {n}º Número: '))
    if valor % 2 == 0:
        s += valor
        c_pares += 1
print(f'Foram digitados {c_pares} pares. A soma destes valores é igual {s}')