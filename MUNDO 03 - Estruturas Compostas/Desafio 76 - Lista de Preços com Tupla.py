# # Arquivo Desafio 76.py
# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ()

while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    produtos += (produto, preco)
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]').upper().strip()[0]
    if resp == 'N':
        break
    
print('=' * 40)
print(f'{'LISTA DE PREÇOS':^40}')
print('=' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos].upper():.<30}', end = ' ')
    else:
        print(f'R$ {produtos[pos]:<10.2f}')
print('=' * 40,'\n\n')
