# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from time import sleep
num = 0
contador = 0
acumulador = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    contador += 1
    acumulador += num
    num = int(input('Digite um número [999 para parar]: '))
print('-=-'*10)   
print('Finalizando...')
print('-=-'*10)
sleep(1)
print(f'''Total de números digitados: {contador}
Soma total de todos os números: {acumulador}
FIM!!!''')
