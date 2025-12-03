# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('''Suas opções: 
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')
jogada_humana = int(input('Qual é a sua escolha? '))
#Validando jogada
if jogada_humana in [1, 2, 3]:
    # Jogada_humana
    if jogada_humana == 1:
        jogada_humana = 'PEDRA'
    elif jogada_humana == 2:
        jogada_humana = 'PAPEL'
    elif jogada_humana == 3:
        jogada_humana = 'TESOURA' 
    
    sleep(1.0)
    print('JO')
    sleep(1.0)
    print('KEN')
    sleep(1.0)
    print('PO!!!')
    sleep(1.0)

    # Jogada do computador
    jogada_computador = randint(1, 3)
    if jogada_computador == 1:
        jogada_computador = 'PEDRA'
    elif jogada_computador == 2:
        jogada_computador = 'PAPEL'
    else: 
        jogada_computador = 'TESOURA' 

    print('-=-' * 10)
    print(f'Computador jogou {jogada_computador}')
    print(f'Jogador jogou {jogada_humana}')
    print('-=-' * 10)
    sleep(1.0)
    
    # Validando vencedor
    if jogada_computador == jogada_humana:
        print('EMPATE!!!')
    elif (jogada_computador == 'PAPEL' and jogada_humana == 'PEDRA') \
        or (jogada_computador == 'TESOURA' and jogada_humana == 'PAPEL') \
        or (jogada_computador == 'PEDRA' and jogada_humana == 'TESOURA'):
        print('COMPUTADOR VENCEU!!!')
    else:
        print('PARABÉNS!!! VOCÊ VENCEU!!!')
    

    
else:
    print('Opção Inválida! Tente Novamente!')
    


