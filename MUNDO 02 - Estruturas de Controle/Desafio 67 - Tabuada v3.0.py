# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

from time import sleep

while True:
    print('=' * 40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 40)
    if num < 0:
        break
    else:
        contador = 1
        while contador <= 10:
            print(f'{num} x {contador} = {num * contador}')
            contador += 1
            sleep(0.5)
print('PROGRAMA FINALIZADO!')
    