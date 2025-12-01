# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + ( 10 - 1 ) * razao # fórmula matemática

# **Fórmula do termo geral:**
# a_n = a_1 + (n - 1) * r
#
# Onde:
# - a_n = n-ésimo termo
# - a_1 = primeiro termo
# - r = razão
# - n = posição do termo na sequência
#
# **Exemplo:**
# Qual é o 10º termo da PA 2, 5, 8, ...?
# a_10 = 2 + (10 - 1) * 3 = 2 + 27 = 29


print('PA =', end= ' ')
for n in range (primeiro_termo, decimo_termo + razao, razao):
    print(f'{n}', end=' -> ')
print('FIM')