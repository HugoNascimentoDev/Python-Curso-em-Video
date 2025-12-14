# # Arquivo Desafio 89.py
# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


from time import sleep
cadastro_alunos = []


while True:
    print(f'{'CADASTRO DE ALUNOS':^50}')
    print('-'*50)
    nome_aluno = input('Nome: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    cadastro_alunos.append([nome_aluno, [nota1, nota2], media])    

    resp = ' '
    while resp not in 'SN':
        print('-'*50)
        resp = input('Quer continuar? ').upper().strip()[0]
        print('-'*50)
    if resp == 'N':
        break
print('-=-'*14,'\n')
print('='*42)
print(f'{'ID':<6}{'NOME':<26}{'MÉDIA':<10}')
for i, aluno in enumerate(cadastro_alunos):
    print(f'{i:<6}{aluno[0].upper():<26}{aluno[2]:>10.2f}')


while True:
    print('='*42)
    num = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if num == 999:
        print('='*42)
        print('<<<<< FINALIZANDO >>>>>')
        sleep(1)
        print('<<<<< VOLTE SEMPRE!!! >>>>>\n\n')
        sleep(1)
        break
    else:
        if num <= len(cadastro_alunos) - 1:
            print(f'Notas de {cadastro_alunos[num][0].upper()}: {cadastro_alunos[num][1]}')
        else:
            print('Aluno não encontrado! Tente Novamente!')


