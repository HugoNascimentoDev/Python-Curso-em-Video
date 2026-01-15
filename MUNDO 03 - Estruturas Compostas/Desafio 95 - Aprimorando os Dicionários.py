# # Arquivo Desafio 95.py
# # Seu código aqui
# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = {}
gols = []
resp = ''


while True:
    contador = 1
    jogador['nome'] = input('Digite o nome do jogador: ').capitalize()
    jogador['qtd_partidas'] = int(input('Quandas partidas fez o jogador(a)? '))
    while contador <= jogador['qtd_partidas']:
        qtd_gols = int(input(f'Quantos gols na {contador}º partida? '))
        gols.append(qtd_gols)
        contador += 1
    jogador['gols'] = gols[:]
    jogador['total_gols'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    print('-' * 60)
    resp = input('Deseja cadastrar outro jogador? [S/N] ').upper().strip()[0]
    print('-' * 60)
    if resp == 'N':
        break
    while resp != 'S':
        print('<<< ERRO >>>> DIGITE UM VALOR VÁLIDO!!!!')
        resp = input('Deseja cadastrar outro jogador? [S/N] ').upper().strip()[0]

print('='*60)
print(jogadores)
print('='*60)

for j in jogadores:
    for k, v in j.items():
        print(f'O {k.upper()} tem o valor {v}.')
    print('-'*60)
print('='*60)
