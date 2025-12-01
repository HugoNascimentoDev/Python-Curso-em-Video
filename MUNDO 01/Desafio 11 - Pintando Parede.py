# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura: (metros) '))
altura = float(input('Altura: (metros) '))

area = largura * altura

print(f'''Largura: {largura} metro(s)
Altura: {altura} metro(s)
Área: {area:.2f} metro(s)
Você vai precisar de {area / 2:.2f} litros de tinta para pintar toda a parede!
''')
