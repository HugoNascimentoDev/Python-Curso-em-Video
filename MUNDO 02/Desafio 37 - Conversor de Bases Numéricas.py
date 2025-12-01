# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número qualquer: '))
print('''Escolha uma opção: 
[1]binário
[2]octal 
[3]hexadecimal
[0]sair''')

opcao = int(input('Escolha sua opção: '))


if opcao == 1:
    print(f'O número {n} é igual a {bin(n)[2:]} binário!')
elif opcao == 2:
    print(f'O número {n} é igual a {oct(n)[2:]} octal!')
elif opcao == 3:
    print(f'O número {n} é igual a {hex(n)[2:]} hexadecimal!')
else:
    print('Opção Inválida! Tente novamente!')
