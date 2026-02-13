# Arquivo Desafio 103.py
# Seu código aqui
# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha (nome_jogador = '<desconhecido>', qtd_gols = 0):
    print(f'O jogador {nome_jogador.upper()} fez {qtd_gols} gol(s) no campeonato!')
    

n_jogador = input('Digite o nome do jogador: ')
q_gols = input('Digite a quantidade de gols: ')

if q_gols.isnumeric():
    q_gols = int(q_gols)
else:
    q_gols = 0

if n_jogador.strip() == '':
    ficha(qtd_gols= q_gols)
else:
    ficha(n_jogador, q_gols)





