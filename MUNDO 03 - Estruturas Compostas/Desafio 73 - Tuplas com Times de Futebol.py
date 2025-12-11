# # Arquivo Desafio 73.py
# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

times_brasileirao_2025 = (
    "FLAMENGO", "PALMEIRAS", "CRUZEIRO", "MIRASSOL", "FLUMINENSE",
    "BOTAFOGO", "BAHIA", "SAO PAULO", "GREMIO", "RB BRAGANTINO",
    "ATLETICO-MG", "SANTOS", "CORINTHIANS", "VASCO DA GAMA", "VITORIA",
    "INTERNACIONAL", "CEARA", "FORTALEZA", "JUVENTUDE", "SPORT"
)
print('='*40) 
print(f'-> Lista de times do Brasileirão 2025:\n{times_brasileirao_2025}')
# a) Os 5 primeiros times.
print('='*40) 
print('-> Os 5 primeiros times')
print(times_brasileirao_2025[:5])

# b) Os últimos 4 colocados.
print('='*40) 
print('-> Os últimos 4 colocados')
print(times_brasileirao_2025[-4:])

# c) Times em ordem alfabética.
print('='*40) 
print('-> Times em ordem alfabética')
print(sorted(times_brasileirao_2025))

# d) Em que posição está o time da Chapecoense.
print('='*40) 
print('-> Adaptando, escolhendo o time e descobrindo sua posição no campeonato!')

while True:
    time = input('Digite o nome do time: ').upper()
    if time in times_brasileirao_2025:
        posicao = times_brasileirao_2025.index(time) + 1
        print(f'O time {time} terminou o campeonato na {posicao}ª posição.')
        break
    else:
        print(f'O time {time} não disputou o Brasileirão Série A 2025. Tente novamente!', end = ' ')
