# # Arquivo Desafio 108.py
# # Seu código aqui

# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda108

n = float(input('Digite um valor: '))
escolha = int(input('Escolha a moeda: [1] - $ ou [2] - R$ '))
if escolha == 1:
    moeda = "$ "
elif escolha == 2:
    moeda = "R$ "
else:
    print('Escolha Moeda Inválida!')


print(f'O valor {moeda108.moeda(n, moeda)} com o aumento de 10% é igual a {moeda108.moeda(moeda108.aumentar(n, 0.10), moeda)}.')
print(f'O valor {moeda108.moeda(n, moeda)} com o desconto de 10% é igual a {moeda108.moeda(moeda108.diminuir(n, 0.10), moeda)}.')
print(f'O dobro do valor {moeda108.moeda(n, moeda)} é igual a {moeda108.moeda(moeda108.dobro(n), moeda)}.')
print(f'A metade do valor {moeda108.moeda(n, moeda)} é igual a {moeda108.moeda(moeda108.metade(n), moeda)}.')