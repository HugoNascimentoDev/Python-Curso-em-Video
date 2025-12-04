# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
from time import sleep

contador = resultado = 0
linha = '='*40
print('Vamos jogar PAR ou ÍMPAR')
print(f'{linha}')

while True:
    pc = randint (1,10)
    jogador = int(input('Escolha um número de 1 a 10: '))
    resultado = pc + jogador
    opcao = int(input('''Escolha: 
    [1] PAR
    [2] ÍMPAR
'''))
    if opcao == 1:
        print('Você escolheu PAR!')
    elif opcao == 2:
        print('Você escolheu ÍMPAR!')
    else: 
        print(f'Opção Inválida! Escolha uma opção válida!\n{linha}')
        continue
    
    resultado = pc + jogador
    print(f'{linha}\nVerificando...\n{linha}')
    sleep(1)
    print(f'''Jogada COMPUTADOR: {pc}
Jogada PLAYER: {jogador}
RESULTADO: {pc} + {jogador} = {resultado}
{linha}''')
    sleep(1)
    if (opcao == 1 and resultado % 2 == 0) or (opcao == 2 and resultado % 2 != 0):
        print(f'Você VENCEU!\n{linha}')
        contador += 1
    else:
        print(f'Você PERDEU!')
        break
   
print(f'{linha}\nGAME OVER! Você venceu {contador} vez(es).\n{linha}')