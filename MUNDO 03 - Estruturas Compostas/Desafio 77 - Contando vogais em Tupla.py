# # Arquivo Desafio 77.py
# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    "FOCO",
    "DISCIPLINA",
    "DEDICACAO",
    "APRENDIZADO",
    "EVOLUCAO",
    "RESILIENCIA",
    "CONFIANCA",
    "PERSISTENCIA",
    "SUPERACAO",
    "VITORIA"
)

for p in palavras:
    print(f'\nA Palavra: {p} temos ', end= '')
    for vogal in p:
        if vogal in 'AEIOU':
            print(f'{vogal}', end = ' ')