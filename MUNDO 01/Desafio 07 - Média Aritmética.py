# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


n1 = float(input('Digite 1ª Nota: '))
n2 = float(input('Digite 2ª Nota: '))

media = (n1 + n2) / 2

print(f'''Resultado:
==============
1ª Nota: {n1}
2ª Nota: {n2}
==============
Média: {media:.1f}
==============      
''')