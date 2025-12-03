#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Digite a temperatura em ºCelcius: '))

conversao = ((9 * temperatura) / 5) + 32

print(f'A temperatura {temperatura}ºC corresponde em {conversao}ºF')