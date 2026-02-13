# # # Arquivo Desafio 104.py
# # # Seu código aqui

# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def leiaInt(msg):
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}.')
            break
        else:
            print('<<< ERRO >>> Digite um número inteiro válido!')
    return int(n)

n = leiaInt('Digite um número: ')


