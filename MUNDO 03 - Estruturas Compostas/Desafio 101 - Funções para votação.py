# # Arquivo Desafio 101.py
# # Seu código aqui

# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

print('-' * 60)
ano = int(input('Digite seu ano de nascimento: [yyyy] '))

def voto (ano = 0):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade >= 70 or idade == 16 or idade == 17:
        status_voto = 'Seu voto é OPCIONAL!'
    elif idade < 16:
        status_voto = 'NÃO VOTA!'
    elif idade >= 18 and idade < 70:
        status_voto = 'Seu voto é OBRIGATÓRIO!'
    else:
        status_voto = '<<< VALOR INVÁLIDO! TENTE NOVAMENTE >>>'
        
    return idade, status_voto

idade, status_voto = voto(ano)

print(f'Com {idade} anos: {status_voto}')
