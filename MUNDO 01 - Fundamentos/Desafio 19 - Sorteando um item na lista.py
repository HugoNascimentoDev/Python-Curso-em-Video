# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno01 = input('Digite o nome do 1º Aluno: ')
aluno02 = input('Digite o nome do 2º Aluno: ')
aluno03 = input('Digite o nome do 3º Aluno: ')
aluno04 = input('Digite o nome do 4º Aluno: ')

sorteado = random.choices([aluno01, aluno02, aluno03, aluno04], k = 1)[0]

print(f'Entre os alunos, {aluno01}, {aluno02}, {aluno03} e o {aluno04}, o aluno sorteado foi o {sorteado}')



from random import choice

n1 = input('Digite o nome do 1º Aluno: ')
n2 = input('Digite o nome do 2º Aluno: ')
n3 = input('Digite o nome do 3º Aluno: ')
n4 = input('Digite o nome do 4º Aluno: ')

alunos = [n1, n2, n3, n4]
escolhido = choice(alunos)

print(f'Entre os alunos, {alunos}, o aluno sorteado foi o {escolhido}')