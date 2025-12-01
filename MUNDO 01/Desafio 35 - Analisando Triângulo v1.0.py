# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('='* 40)
print('Analisando Triângulos...')
print('='* 40)
l1 = int(input('Digite o tamanho do 1º lado: '))
l2 = int(input('Digite o tamanho do 2º lado: '))
l3 = int(input('Digite o tamanho do 3º lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print(f'É possivel formar um triângulo!')
else:
    print(f'Não é possivel formar um triângulo!')