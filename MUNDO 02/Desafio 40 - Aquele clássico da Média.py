# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO


n1 = float(input('Digite 1ª Nota: '))
n2 = float(input('Digite 2ª Nota: '))

media = (n1 + n2) / 2

print(f'Sua média foi: {media}', end=' ')
if media >= 7:
    print(f'PARABÉNS! Você foi APROVADO!')
elif media <= 6.9 and media >= 5:
    print(f'Estude MAIS! Você está em RECUPERAÇÃO!')
else:
    print(f'Infelizmente você foi REPROVADO!')