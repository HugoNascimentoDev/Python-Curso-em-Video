# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 
tot_pessoas_maior_dezoito = tot_homens = tot_mulher_menor_vinte = tot_cadastros = 0
linha = '=' * 37

while True:
    print(linha)
    print('\tCADASTRE UMA PESSOA')
    print(linha)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    if sexo == 'M':
        tot_homens += 1
    if idade > 18:
        tot_pessoas_maior_dezoito += 1
    if sexo == 'F' and idade < 20:
        tot_mulher_menor_vinte += 1
    print(linha)
    tot_cadastros += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N] ').upper().strip()[0]
    if opcao == 'N':
        break

print(f'''{linha}\n\t\tRESUMO\n{linha}
Total de pessoas cadastrada: {tot_cadastros}
Total de pessoas com mais de 18 anos: {tot_pessoas_maior_dezoito}
Ao todo temos {tot_homens} homen(s) cadastrados
E temos {tot_mulher_menor_vinte} mulher(es) com menos de 20 anos.\n\n''')