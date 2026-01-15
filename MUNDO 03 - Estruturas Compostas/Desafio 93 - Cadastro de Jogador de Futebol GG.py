# # Arquivo Desafio 93.py
# # Seu código aqui
# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []

jogador['nome'] = input('Nome do jogador: ').capitalize()
tot = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
for c in range (1, tot + 1):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total_gols'] = sum(partidas)

print('=' * 60)
print(jogador)
print('=' * 60)

for k, v in jogador.items():
    print(f'O campo {k.upper()} tem o valor {v}.')
print('=' * 60)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partida(s).')
print('=' * 60)

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print('=' * 60)
print(f'Foi um total de {jogador["total_gols"]} gol(s) marcados.')
print('=' * 60)