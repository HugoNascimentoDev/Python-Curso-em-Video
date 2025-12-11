# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
linha = '=' * 50
print(linha)
print('\t\tBANCO NASCIMENTO')
print(linha)
valor = 0
valor = int(input('Qual o valor deseja sacar? '))
print(linha)
total = valor
cedula = 100
contador_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        contador_cedula += 1
    else:
        if contador_cedula > 0:
            print(f'Total de {contador_cedula} cédulas de R$ {cedula:.2f}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        contador_cedula = 0
        if total == 0:
            break
print(linha)
print('Volte sempre ao BANCO NASCIMENTO! Tenha um bom dia!\n\n')