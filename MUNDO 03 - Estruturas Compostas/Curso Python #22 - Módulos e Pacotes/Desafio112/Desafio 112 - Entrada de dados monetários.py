# # Arquivo Desafio 108.py
# # Seu código aqui

# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from Treinando import moeda, dado

n = dado.leiaDinheiro('Digite o valor em R$: ')

moeda.resumo(n, 0.10, 0.15)

