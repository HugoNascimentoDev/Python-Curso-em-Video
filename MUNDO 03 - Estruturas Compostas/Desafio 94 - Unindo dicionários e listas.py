# # Arquivo Desafio 94.py
# # Seu código aqui
# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


lista = []

condicao = ''

while True:
    condicao = input('Deseja cadastrar? [S/N] ')
    if condicao in 'Ss':
        dados = {}
        dados['nome'] = input('Digite o nome: ').capitalize()
        dados['sexo'] = input('Digite o sexo: [M/F] ').strip().upper()[0]
        dados['idade'] = int(input('Digite a idade: '))

        lista.append(dados.copy())
    else:
        break
print('=' * 60)
print(lista)
print('=' * 60)
# A) Quantas pessoas foram cadastradas
print(f'Foram cadastradas o total de {len(lista)} pessoas.')
print('=' * 60)
#B) A média de idade
total_idade = 0

for p in lista:
    total_idade = total_idade + p['idade']

media = total_idade / len(lista)

print(f'O total das idades é de {total_idade}.\nA Média das idades é de {media:.2f}')


print('=' * 60)
# C) Uma lista com as mulheres
lista_mulheres = []

for p in lista:
    if p['sexo'] == 'F':
        lista_mulheres.append(p['nome'])
print(f'Lista de mulheres: {lista_mulheres}')

print('=' * 60)
# D) Uma lista de pessoas com idade acima da média
acima_media = []

for p in lista:
    if p['idade'] > media:
        acima_media.append(p['nome'])

print(f'Lista de pessoas acima da média de idade: {acima_media}')

print('=' * 60)