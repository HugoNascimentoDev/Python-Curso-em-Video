# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt

cateto_oposto = float(input("Digite o valor do Cateto Oposto: "))
cateto_adjacente = float(input("Digite o valor do Cateto Adjacente: "))
hipotenusa = sqrt(cateto_adjacente**2 + cateto_oposto**2)

print(f'''Cateto Oposto = {cateto_oposto}
Cateto Adjacente = {cateto_adjacente}
Hipotenusa = {hipotenusa:.2f}
''')


from math import hypot

cateto_oposto2 = float(input("Digite o valor do Cateto Oposto: "))
cateto_adjacente2 = float(input("Digite o valor do Cateto Adjacente: "))
hipotenusa2 = hypot(cateto_oposto2, cateto_adjacente2)

print(f'''Cateto Oposto = {cateto_oposto2}
Cateto Adjacente = {cateto_adjacente2}
Hipotenusa = {hipotenusa2:.2f}
''')
