# # Arquivo Desafio 92.py
# # Seu código aqui
# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

cadastro_pessoa = {}

cadastro_pessoa['nome'] = input('Digite um nome: ')
cadastro_pessoa['ano_nascimento'] = int(input('Digite o ano de nascimento: '))
cadastro_pessoa['ano_atual'] = datetime.now().year
cadastro_pessoa['idade'] = cadastro_pessoa['ano_atual'] - cadastro_pessoa['ano_nascimento']

cadastro_pessoa['carteira_trabalho'] = int(input('Nr da carteira de trabalho (0 não tem): '))

if cadastro_pessoa['carteira_trabalho'] != 0:
    cadastro_pessoa['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    cadastro_pessoa['salario'] = float(input('Digite o valor do salário: R$ '))
    cadastro_pessoa['idade_aposentadoria'] = 35 - (cadastro_pessoa['ano_atual'] - cadastro_pessoa['ano_contratacao']) + cadastro_pessoa['idade']
    cadastro_pessoa['ano aposentadoria'] = cadastro_pessoa['ano_contratacao'] + 35
    
print('=' * 60)
for k, v in cadastro_pessoa.items():
    print(f'- {k} tem o valor {v}')
print('=' * 60)
    

