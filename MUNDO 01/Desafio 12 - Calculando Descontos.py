#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


preco_produto = float(input('Digite o valor: '))

print(f'''Preço atual do produto R$ {preco_produto:.2f}
Novo preço R$ {preco_produto * 1.05}
Aumento (5%) R$ {((preco_produto * 1.05) - preco_produto):.2f}''')