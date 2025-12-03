# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu sálario: '))

if salario > 1250:
    perc_aumento = 0.10
else:
    perc_aumento = 0.15

novo_salario = salario + (salario * perc_aumento)

print(f'''Salário atual: R$ {salario:.2f}
% aumento: {perc_aumento:.2%}
Valor aumento: R$ {salario * perc_aumento:.2f}
Novo Salário: R$ {novo_salario:.2f}
''')