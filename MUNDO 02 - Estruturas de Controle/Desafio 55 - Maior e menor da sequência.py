# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

qtd_cadastros = int(input('Quantos cadastros deseja realizar? '))

maior_peso = menor_peso = 0

for pessoa in range (1, qtd_cadastros + 1):
    peso_pessoa = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior_peso = peso_pessoa
        menor_peso = peso_pessoa
    else:
        if maior_peso < peso_pessoa:
            maior_peso = peso_pessoa
        if menor_peso > peso_pessoa:
            menor_peso = peso_pessoa

print(f'O MAIOR peso foi: {maior_peso}')
print(f'O MENOR peso foi: {menor_peso}')