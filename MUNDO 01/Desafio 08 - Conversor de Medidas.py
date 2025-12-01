#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.


metros = float(input("Digite a quantidade em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f'''CONVERSOR: 
Metros: {metros:.2f} m(s)
Centimetros: {centimetros:.2f} cm(s)
Milimetros: {milimetros:.2f} mm(s)
''')