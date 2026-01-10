# # Arquivo Desafio 90.py
# # Seu código aqui
# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos['nome'] = input('Digite o nome do aluno: ')
alunos['media'] = float(input(f'Digite a nota do aluno {alunos["nome"].upper()}:'))

if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado!!! 😁'
elif alunos['media'] >= 5:
    alunos['situacao'] = 'Em Recuperação!!! 😯'
else:
    alunos['situacao'] = 'Reprovado!!! 😤'

print('=' * 40)

for k, v in alunos.items():
    print(f'    - {k.capitalize()} é igual a {v}.')

print('=' * 40)
