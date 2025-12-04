# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

acumulador = contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        acumulador += num
        contador += 1
    else:
        break

print(f'A soma dos {contador} valores foi {acumulador}.')
