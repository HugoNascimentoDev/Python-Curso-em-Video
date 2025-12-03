# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais


from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print('Pensando...')
sleep(1.5)

if n1 > n2:
    print(f'O {n1} é maior do que {n2}.')
elif n2 > n1:
    print(f'O {n2} é maior do que {n1}.')
else:
    print(f'Os dois valores ({n1} e {n2}) são IGUAIS.')