#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere a US$ 1 = R$ 5.30

dinheiro_real = float(input('Digite quanto dinheiro você possui: R$ '))

taxa_dolar = 5.30

print(f'Com R$ {dinheiro_real:.2f} você pode comprar US$ {dinheiro_real / taxa_dolar:.2f}')