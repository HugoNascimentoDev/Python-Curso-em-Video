# # Arquivo Desafio 95.py
# # Seu código aqui
# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados_jogadores = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = input('Nome do jogador: ').capitalize()
    tot = int(input(f"Quantas partidas fez o {jogador['nome']} jogou? "))
    for c in range (1, tot + 1):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total_gols'] = sum(partidas)
    dados_jogadores.append(jogador.copy())
    print('-'*60)
    while True:
        resp = input('Quer cadastrar outro jogador? [S/N] ').strip().upper()[0]
        print('-'*60)
        if resp in 'SN':
            break
        print('<<<<< ERRO >>>>> Responda apenas S ou N.')
        print('-'*60)
    if resp == 'N':
        break
print('=' * 60)
print(dados_jogadores)
print('=' * 60)
print('=' * 60)
print(jogador)
print('=' * 60)

for j in dados_jogadores:
    for k, v in j.items():
        print(f'O campo {k.upper()} tem o valor {v}.')
    print('=' * 60)
    print(f'O jogador {j["nome"]} jogou {len(j["gols"])} partida(s).')
    print('=' * 60)

    for i, v in enumerate(j['gols']):
        print(f'    => Na partida {i}, fez {v} gols.')
    print('=' * 60)
    print(f'Foi um total de {j["total_gols"]} gol(s) marcados.')
    print('=' * 60)

print('COD ', end = '')
for i in jogador.keys():
    print(f'{i.upper():<15}', end ='')
print()
print('-' * 60)
for k, v in enumerate(dados_jogadores):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
print('=' * 60)

while True:
    print('-' * 60)
    busca = int(input('Digite o código do jogador para buscar o detalhamento de dados ou 999 para parar: '))
    if busca == 999:
        break
    if busca >= len(dados_jogadores):
        print(f'ERRO!!! O jogador escolhido com o código {busca} não existe!!! Tente Novamente!!! ')
    else:
        print('-' * 60)
        print(f'    --- LEVANTAMENTO DO JOGADOR {dados_jogadores[busca]["nome"].upper()}: ')
        print('-' * 60)
        for i, g in enumerate(dados_jogadores[busca]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gols.')
print('=' * 60)

print('<<< VOLTE SEMPRE >>>')
