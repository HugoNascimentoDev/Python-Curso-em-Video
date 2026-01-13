# # Arquivo Desafio 93.py
# # Seu código aqui
# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}

jogador['nome'] = input('Nome do jogador: ')
jogador['qtd_partidas'] = int(input(f'Quantas partidas o jogador(a) {jogador["nome"].upper()} jogou? '))
jogador['total_gols'] = 0
contador = 1
lista_gols = []

while contador <= jogador['qtd_partidas']:
    qtd_gols = int(input(f'Quantos gols na partida {contador}: '))
    lista_gols.append(qtd_gols)
    contador += 1

jogador['total_gols'] = sum(lista_gols)
jogador['gols'] = lista_gols

print('='*60)
print(jogador)
print('='*60)

for k, v in jogador.items():
    print(f'O campo {k.upper()} tem o valor {v}. ')
print('='*60)

print(f'O jogador {jogador["nome"].upper()} jogou o total de {jogador["qtd_partidas"]} partida(s) e fez o total de {jogador["total_gols"]} gol(s).')
for c in range (1, jogador['qtd_partidas'] + 1):
    print(f'=> Na partida {c}, fez {jogador["gols"][c - 1]} gol(s).')

print('='*60)


