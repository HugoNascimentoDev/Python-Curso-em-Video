# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ').upper().strip()
palavras_separadas = frase.split() #cria uma lista com cada palavra
palavras_unidas = ''.join(palavras_separadas) #junta todas as palavras da lista SEM espaço entre elas
inverso = ''
for letra in range (len(palavras_unidas) -1, -1, -1): # percorre a variavel palavras unidas de trás para frente
    inverso += palavras_unidas[letra] # adiciona cada letra da variavel a nova variavel criada (inverso)

if palavras_unidas == inverso:
    print(f'{inverso} é IGUAL a {palavras_unidas}! Portanto é um PALÍNDROMO!')
else:
    print(f'{inverso} é DIFERENTE a {palavras_unidas}! Portanto é um NÃO É PALÍNDROMO!')






