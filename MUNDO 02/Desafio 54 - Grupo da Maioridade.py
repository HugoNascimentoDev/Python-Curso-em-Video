# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year # verificando o ano atual
# print(ano_atual)
idade = 0
i_maior = i_menor = 0
lista_anos = []
lista_idade = []
for n in range (1, 8):
    ano_nascimento = int(input(f'Digite a idade da {n}º pessoa: '))
    lista_anos.append(ano_nascimento)
    idade = ano_atual - ano_nascimento
    lista_idade.append(idade)
    if idade >= 21:
        i_maior += 1
    else:
        i_menor += 1

print(f'''Anos cadastrados: {lista_anos}
Idades cadastradas: {lista_idade}
Total pessoas MAIORES de idade: {i_maior}
Total pessoas MENORES de idade: {i_menor}
''')
