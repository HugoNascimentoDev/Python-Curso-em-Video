# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = acumulador = maior = menor = 0
resp = 'S'

while resp in 'S':
    num = int(input('Digite um número: '))
    contador += 1
    acumulador += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num    
    resp = input('Deseja continuar [S/N]: ').strip().upper()[0]

media = acumulador / contador

print(f'''MAIOR valor: {maior}
MENOR valor: {menor}
CONTADOR: {contador}
SOMA TOTAL: {acumulador}
MÉDIA: {media:.2f}''')


