# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

qtd_pessoas = int(input("Quantos cadastros deseja realizar? "))

s_idade = qtd_mulheres_menores_20 = idade_homem_mais_velho = 0
homem_mais_velho = ''

for pessoa in range(1, qtd_pessoas + 1):
    print('=' * 5, f' {pessoa} PESSOA ', '='*5)
    nome = input('NOME: ').upper().strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO[M/F]: ').upper().strip()
    s_idade += idade
    if sexo in 'Ff' and idade < 20:
        qtd_mulheres_menores_20 += 1
    if sexo in 'Mm':
        if pessoa == 1:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
        else:
            if idade > idade_homem_mais_velho:
                homem_mais_velho = nome
                idade_homem_mais_velho = idade


media_idade = s_idade / qtd_pessoas

print('='*22, f'''
Média de idades: {media_idade:.2f}
Homem mais velho: {homem_mais_velho}
Quantidade de Mulheres MENORES de 20 anos: {qtd_mulheres_menores_20}''')