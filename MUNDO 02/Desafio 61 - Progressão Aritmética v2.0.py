# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PROGRESSÃO ARITMÉTICA')
print('=' * 35)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end= '')
    termo += razao
    contador += 1
print('FIM')