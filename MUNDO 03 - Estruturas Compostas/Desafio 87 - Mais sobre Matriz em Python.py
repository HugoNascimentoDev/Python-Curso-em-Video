# # Arquivo Desafio 87.py
# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

acumulador = soma_terceira_coluna = soma_segunda_linha = maior_valor_segunda_linha = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [ {linha} , {coluna} ]: '))
        # A) A soma de todos os valores pares digitados.
        if matriz [linha][coluna] % 2 == 0:
            acumulador += matriz [linha][coluna]
print('-=-'*15)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^7}]', end = ' ')
    print(f'')
print('-=-'*15)

# A) A soma de todos os valores pares digitados.
print(f'Soma dos valores pares: {acumulador}')

# B) A soma dos valores da terceira coluna.
for linha in range(0,3):
    soma_terceira_coluna += matriz[linha][2]

print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')

# C) O maior valor da segunda linha.
for coluna in range(0, 3):
    soma_segunda_linha += matriz[1][coluna]
    if coluna == 0:
        maior_valor_segunda_linha = matriz[1][coluna]
    else:
        if matriz[1][coluna] > maior_valor_segunda_linha:
            maior_valor_segunda_linha = matriz[1][coluna]

print(f'Soma dos valores segunda linha: {soma_segunda_linha}')
print(f'O maior valor da segunda linha: {maior_valor_segunda_linha}')