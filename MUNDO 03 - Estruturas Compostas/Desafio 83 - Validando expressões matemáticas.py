# # Arquivo Desafio 83.py
# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Arquivo Desafio 83.py
# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# O aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

# Solicita ao usuário que digite uma expressão
expressao = input('Digite uma expressão: ')

# Criamos uma lista chamada "pilha" que será usada para controlar os parênteses
pilha = []

# Percorremos cada símbolo da expressão digitada
for simb in expressao:
    if simb == '(':  
        # Se o símbolo for um parêntese aberto, adicionamos na pilha
        pilha.append('(')
    elif simb == ')':  
        # Se for um parêntese fechado:
        if len(pilha) > 0:
            # Se houver algum parêntese aberto na pilha, removemos (fechamos)
            pilha.pop()
        else:
            # Se não houver nada para fechar, significa que a ordem está errada
            pilha.append(')')
            break  # já podemos parar, pois a expressão é inválida

# Após percorrer toda a expressão:
if len(pilha) == 0:
    # Se a pilha estiver vazia, todos os parênteses foram fechados corretamente
    print('Sua expressão é válida!')
else:
    # Se ainda restar algo na pilha, significa que há parênteses sem fechamento
    print('Sua expressão é inválida!')
