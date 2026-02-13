# # Arquivo Desafio 105.py
# # Seu código aqui

# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas (*n, sit = False):
    ''' -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionarário com várias informações sobre a situação da turma.
    '''
    resumo_notas = {}

    if len(n) != 0:
        qtd_total_notas = len(n)
        resumo_notas['Quantidade de notas'] = qtd_total_notas

        maior_nota = max(n)
        resumo_notas['Maior nota'] = maior_nota
        menor_nota = min(n)
        resumo_notas["Menor nota"] = menor_nota

        media_nota_turma = sum(n) / qtd_total_notas
        resumo_notas['Media da turma'] = media_nota_turma

        if sit:
            if media_nota_turma <= 5:
                situacao = "RUIM"
            elif media_nota_turma <= 7:
                situacao = "RAZOAVEL"
            elif media_nota_turma <= 9:
                situacao = "BOA"
            else:
                situacao = "EXCELENTE"
            resumo_notas["Situação"] = situacao
    else:
        print('Você deve informar ao menos o valor de uma nota!')

    return resumo_notas


resp = notas(7.9, 2.5, 9.0, 10.0, 9, 3, sit = True)
print(resp)

help(notas)