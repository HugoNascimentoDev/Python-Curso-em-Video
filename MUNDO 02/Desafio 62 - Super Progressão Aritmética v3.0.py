# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


print('Gerador de PROGRESSÃO ARITMÉTICA')
print('=' * 35)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
mais_termos = 10

while mais_termos != 0:
    total = total + mais_termos
    while contador <= total:
        print(f'{termo} -> ', end= '')
        termo += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos mais você gostaria? '))
print(f'Total de termos {total} exibidos!')

