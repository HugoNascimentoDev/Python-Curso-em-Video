# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))

opcao = 0

while opcao != 5:
    print('''========== MENU ==========
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
==========================''')
    opcao = int(input('Digite uma opção: '))
    print('==========================')
    sleep(1)
    if opcao == 1:
        print(f'''Você selecionou a opção: 
========== SOMA ==========
{v1} + {v2} = {v1 + v2}''')
        
    elif opcao == 2:
        print(f'''Você selecionou a opção: 
====== MULTIPLICAÇÃO =====
{v1} x {v2} = {v1 * v2}''')

    elif opcao == 3:
        if v1 > v2:
            print(f'Entre {v1} e o {v2}, o MAIOR número é o {v1}.')
        elif v1 < v2:
            print(f'Entre {v1} e o {v2}, o MAIOR número é o {v2}.')
        else:
            print(f'Os números {v1} e {v2} são iguais!')

    elif opcao == 4:
        print('Digite os novos números: ')
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else: 
        print('Opção Inválida! Escolha corretamente:')
    

print('==========================')
print('Fim do programa! Volte sempre!')