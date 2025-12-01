#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input('Digite o salário: '))

novo_salario = salario * 1.15
aumento = novo_salario - salario

print(f'''Salário: R$ {salario:.2f}
Aumento: R$ {aumento:.2f}
Novo Salário: R$ {novo_salario:.2f}
''')