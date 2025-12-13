# # Arquivo Desafio 82.py
# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

c = 0
while True:
    num = int(input(f'Digite o {c +1}º número: '))
    numeros.append(num)
    c += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=-'*20)
print(f'''Lista números: {numeros}
Números pares: {pares}
Números ímpares: {impares}''')