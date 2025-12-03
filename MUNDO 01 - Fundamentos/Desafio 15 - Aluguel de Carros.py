#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantos KM(s) percorridos: '))
dias = int(input('Quantos dia(s) de aluguel: '))

por_km = 0.15
por_dia = 60

total = (km * por_km) + (dias * por_dia)

print(f'''===================================
CUSTO ALUGUEL DE VEICULOS
===================================
DIA(s) alugado: {dias}
KM(s) percorridos: {km}
===================================
Custo por dia: R$ {dias * por_dia:.2f}
Custo por KM: R$ {km * por_km:.2f}
===================================
TOTAL: R$ {total:.2f}
''')