# Arquivo Desafio 97.py
# Seu código aqui
# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Ex: 
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva():
    texto = input('Digite um texto: ')
    qtd_final = (int(len(texto)) + 6)
    print('~' * qtd_final)
    print(f'{texto:^{qtd_final}}')
    print('~' * qtd_final)

escreva()


