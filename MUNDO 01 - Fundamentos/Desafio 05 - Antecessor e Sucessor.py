#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.


num = int(input('Digite um número: '))

print(f'''Número: {num}
Sucessor: {num + 1}
Antecessor: {num - 1}
      ''')