# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

pc = randint(0, 10)
print('Vamos brincar? Adivinhe um número entre 0 e 10 que estou pensando....')
sleep(1)
cont_jogadas = 1
jogador = int(input('Faça a sua jogada: '))
sleep(1)
while pc != jogador:
    if pc > jogador:
        print('Mais... Tente mais uma vez!')
    if pc < jogador:
        print('Menos... Tente mais uma vez!')
    jogador = int(input('Digite um número: '))
    cont_jogadas += 1
    sleep(1)

print(f'''
PARABÉNS! Você ACERTOU! 
TENTATIVAS: {cont_jogadas}
COMPUTADOR: {pc}
JOGADOR: {jogador}
''')