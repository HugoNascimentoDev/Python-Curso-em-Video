# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite sua  velocidade: '))

if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print(f'Você ultrapossou o limite de velocidade de 80 Km/h, será multado em R$ {multa:.2f} ')
else:
    print(f'PARABÉNS! Você dirigiu dentro do limite de velocidade! ')
