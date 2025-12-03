# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').strip().upper()
print(f'Nome completo: {nome}')

separado = nome.split()

print(f'''Primeiro nome: {separado[1]}
Último nome: {separado[-1]}
''')