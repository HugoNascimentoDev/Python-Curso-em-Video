# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


from random import choice, shuffle

n1 = input('Digite o nome do 1º Aluno: ')
n2 = input('Digite o nome do 2º Aluno: ')
n3 = input('Digite o nome do 3º Aluno: ')
n4 = input('Digite o nome do 4º Aluno: ')

alunos = [n1, n2, n3, n4]

shuffle(alunos)

print(f'A ordem de apresentação sorteado foi o {alunos}')