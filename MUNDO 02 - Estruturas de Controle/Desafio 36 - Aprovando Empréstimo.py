# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Qual o valor do seu salário? '))
tempo_financiamento = int(input('Em quanto tempo(ano) deseja financiar sua casa? '))

valor_prestacao = valor_casa / (tempo_financiamento * 12)
limite_financiamento = salario_comprador * 0.30

if valor_prestacao <= limite_financiamento:
    print('Parabéns, você teve seu financiamento aprovado!')
else:
    print('Infelizmente não foi desta vez, seu financiamento foi negado!')