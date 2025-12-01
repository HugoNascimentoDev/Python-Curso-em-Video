#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite o valor: '))

print(f'''
========================      
TABUADA DE {num}
========================
{num} x 1 = {num * 1}
{num} x 2 = {num * 2}
{num} x 3 = {num * 3}
{num} x 4 = {num * 4}
{num} x 5 = {num * 5}
{num} x 6 = {num * 6}
{num} x 7 = {num * 7}
{num} x 8 = {num * 8}
{num} x 9 = {num * 9}
{num} x 10 = {num * 10}
========================
''')