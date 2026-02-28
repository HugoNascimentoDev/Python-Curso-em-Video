# # Arquivo Desafio 113.py
# # Seu código aqui
# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        n = input(msg)
        try:
            n = int(n)
            print(f'Você acabou de digitar o número {n}')
            return n
        except (ValueError, TypeError):
            print(f'<<< ERRO >>> Digite um número inteiro válido! ')
            continue
        except (KeyboardInterrupt):
            print(f'<<< ERRO >>> Entrada de dados interrompida! ')
            return 0
        
            

def leiaFloat(msg):
    while True: 
        n = input(msg)
        try:
            n = n.replace(',','.')
            n = float(n)
            print(f'Você acabou de digitar o número {n}')
            return n
        except (ValueError, TypeError):
            print(f'<<< ERRO >>> Digite um número inteiro válido! ')
            continue
        except (KeyboardInterrupt):
            print(f'<<< ERRO >>> Entrada de dados interrompida! ')
            return 0
        
            



n = leiaInt("Digite um número inteiro: ")
n = leiaFloat('Digite um número float: ')



