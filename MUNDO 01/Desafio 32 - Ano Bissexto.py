# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Digite o ano ou coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} NÃO é bissexto!')

