# # Arquivo Desafio 72.py
# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito", "dezenove",
    "vinte"
)

num = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {num} que por extenso é "{numeros[num].upper()}".')
    else:
        print('Valor Inválido! Tente novamente!', end = ' ')
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if resp == 'N':
        break
