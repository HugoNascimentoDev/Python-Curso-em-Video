# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. # Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print(f'Quem nasceu em {ano} e tem em {ano_atual}, {idade} anos.')
if idade < 18:
    falta = 18 - idade
    print(f'Você tem {idade} anos e falta {falta} anos para você se alistar!')
elif idade > 18:
    ultrapassou = idade - 18
    print(f'Você tem {idade} anos e ultrapassou {ultrapassou} anos, corra para se alistar!')
else:
    print(f'Você tem {idade} anos e deve correr para se alistar!')