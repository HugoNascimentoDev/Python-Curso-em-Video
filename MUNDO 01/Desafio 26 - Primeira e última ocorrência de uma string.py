# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().upper()

print(f'Letra A: {frase.count('A')} vezes')
print(f'1º Letra A: {frase.find('A') + 1}')
print(f'Última Letra A: {frase.rfind('A') + 1}')
