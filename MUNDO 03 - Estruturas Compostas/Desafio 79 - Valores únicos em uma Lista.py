# # Arquivo Desafio 79.py
# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

lista = []

while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print(f'O número {num} foi adicionado com sucesso!')
    else:
        print(f'O número {num} já consta na lista e não foi adicionado! Tente outro número!')
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N]').upper().strip()[0]
    if resp == 'N':
        break

maior = max(lista)
menor = min(lista)
total = sum(lista)
contador = len(lista)
crescente = sorted(lista)
decrescente = sorted(lista, reverse= True)

print(f'''A lista final é composta de: {lista}
O maior número: {maior}
O menor número: {menor}
A soma de todos os números digitados: {total}
A quantidade total de números digitados: {contador}
Lista em ordem crescente: {crescente}
Lista em ordem descrente: {decrescente}
''')
