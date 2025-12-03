# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes


# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('='* 40)
print('Analisando Triângulos...')
print('='* 40)
l1 = int(input('Digite o tamanho do 1º lado: '))
l2 = int(input('Digite o tamanho do 2º lado: '))
l3 = int(input('Digite o tamanho do 3º lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print(f'É possivel formar um triângulo!', end=' ')
    if l1 == l2 == l3:
        print('O triângulo é EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('O triângulo é ESCALENO!')
    else:
        print('O triângulo é ISÓSCELES!')
else:
    print(f'Não é possivel formar um triângulo!')