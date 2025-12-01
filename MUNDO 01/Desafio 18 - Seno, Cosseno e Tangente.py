# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo = float(input("Digite o valor do ângulo: "))
radiano = radians(angulo)

print(f'''Ângulo: {angulo}
Radiano: {radiano:.2f}
Seno: {sin(radiano):.2f}
Cosseno: {cos(radiano):.2f}
Tangente: {tan(radiano):.2f}
''')


