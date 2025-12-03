# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo: [M/F]').upper().strip()[0]

while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]
if sexo == 'M':
    print('Você escolheu MASCULINO!')
elif sexo == 'F':
    print('Você escolheu FEMININO!')
