# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint

pc = randint(1, 5)

jogador = int(input("Escolha um número de 1 à 5: "))

print('Pensando...')
sleep(1.5)


if pc == jogador:
    print('Você VENCEU!!!')
else:
    print('Você PERDEU!!!')

sleep(1.5)
print(f'''Jogador: {jogador}
PC: {pc}''')
