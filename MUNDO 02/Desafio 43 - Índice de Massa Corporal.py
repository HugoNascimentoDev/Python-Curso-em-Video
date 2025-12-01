# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso // (altura**2)

print(f'''
Seu peso atual: {peso}
Sua altura atual: {altura}
Seu IMC atual: {imc}
STATUS: ''', end='')
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal!')
elif imc <= 30:
    print('Sobrepeso!')
elif imc <= 40:
    print('Obesidade!')
else:
    print(f'Cuidado!!! Obesidade Mórbida!!!')