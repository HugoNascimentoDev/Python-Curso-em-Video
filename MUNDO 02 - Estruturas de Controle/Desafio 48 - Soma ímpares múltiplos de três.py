# Exercício Python 048: Faça um programa que calcule a soma entre todos os números ímpares e que são múltiplos de três e que se encontram no intervalo de 1 até 500.

c = 0
s = 0
for n in range (1, 501):
    if n % 3 == 0 and not n % 2 == 0:
        c += 1
        s += n
        print(n, end= ' ')
print('\n')
print(f'Foram solicitados {c} números.')
print(f'A soma total é {s}.')