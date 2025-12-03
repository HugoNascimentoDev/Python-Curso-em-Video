# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = int(input('Digite a distância percorrida: '))

if distancia <= 200:
    preco_km = 0.50
else:
    preco_km = 0.45

print(f'''Sua viagem percorrida: {distancia} KMs
Valor pago por KM: R$ {preco_km:.2f}
Valor final da passagem: R$ {distancia * preco_km:.2f}
''')