# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print("-=-"*5, ' Lojas Nascimento ', "-=-"*5)
preco_produto = float(input('Digite o preço do produto: '))
print('''Escolha a forma de pagamento: 
[1] À VISTA - dinheiro/cheque (10% de desconto)
[2] À VISTA - cartão (05% de desconto)
[3] Compra parcelada - cartão
[0] SAIR      
''')

# 2x no cartão (preço normal)
# 3x ou mais no cartão (20"%" de juros)

opcao = int(input('Opção: '))

if opcao == 1:
    tx_desconto = 0.10
    desconto = preco_produto * tx_desconto
    novo_preco = preco_produto - desconto
    print(f'Sua compra recebeu um desconto de R$ {desconto:.2f}')
elif opcao == 2:
    tx_desconto = 0.05
    desconto = preco_produto * tx_desconto
    novo_preco = preco_produto - desconto
    print(f'Sua compra recebeu um desconto de R$ {desconto:.2f}')
elif opcao == 3:
    qtdparcelas = int(input('Digite o total de parcelas desejadas: '))
    if qtdparcelas == 1 or qtdparcelas == 2:
        novo_preco = preco_produto
        parcela = novo_preco / qtdparcelas
    elif qtdparcelas in [3, 4, 5, 6, 7, 8, 9, 10]:
        tx_juros = 0.20
        total_juros = preco_produto * tx_juros
        novo_preco = preco_produto + total_juros
        parcela = novo_preco / qtdparcelas
    print(f'Sua compra R$ {novo_preco:.2f} foi parcelada em {qtdparcelas} x de R$ {parcela:.2f}, total de juros R$ {total_juros:.2f}')
elif opcao == 0:
    novo_preco = preco_produto
    print('Obrigado! Volte Sempre!')
else:
    print('Opção Inválida!')

print(f'Sua compra de R$ {preco_produto:.2f}, vai custar no final R$ {novo_preco:.2f}')


