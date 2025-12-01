# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Em que cidade você nasceu? ').upper().strip()
cidade2 = cidade
cidade = cidade.split()
print(cidade)
print('SANTO' in cidade[0])

# ou

print(cidade2[:5] == "SANTO")
