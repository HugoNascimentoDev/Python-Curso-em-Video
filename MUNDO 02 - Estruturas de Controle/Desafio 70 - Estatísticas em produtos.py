# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 


linha = '=' * 35

print(linha)
print('\tLOJAS NASCIMENTO')
print(linha)
contador = acumulador = mais_mil = preco_mais_barato = 0
nome_produto_mais_barato = ' '

while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$ '))
    print(linha)
    acumulador += preco
    contador += 1
    resp = ' '
    if preco > 1000: 
        mais_mil += 1
    if contador == 1:
        nome_produto_mais_barato = produto
        preco_mais_barato = preco
    else:
        if preco < preco_mais_barato:
            nome_produto_mais_barato = produto
            preco_mais_barato = preco
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]? ').upper().strip()[0]
        print(linha)
    if resp == 'N':
        break
print(f'\t    RESUMO\n{linha}')
print(f'Total Gasto R$ {acumulador:.2f}')
print(f'Total de produtos mais caro que R$ 1000,00, {mais_mil} produtos.')
print(f'O produto {nome_produto_mais_barato.upper()} é o item mais barato, custando R$ {preco_mais_barato:.2f}\n{linha}\n')

