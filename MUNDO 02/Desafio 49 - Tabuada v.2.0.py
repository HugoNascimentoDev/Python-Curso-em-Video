# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite o valor da tabuada: '))
c = 0

print(f'''=====================      
    TABUADA DE {n}
=====================''')
for num in range (1, 11):
    print(f'{n} x {num} = {num * n}')
print('=====================')
