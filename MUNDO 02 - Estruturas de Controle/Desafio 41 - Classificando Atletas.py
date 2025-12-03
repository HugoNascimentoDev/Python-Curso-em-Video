# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print(f'Estamos no ano de {ano_atual} e você nasceu em {ano}, sua idade é {idade} anos.')

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')