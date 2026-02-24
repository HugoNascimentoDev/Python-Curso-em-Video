# # Arquivo Desafio 108.py
# # Seu código aqui

# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda109

n = float(input('Digite um valor: '))

while True:
    escolha = input('Deseja formatar como moeda? [S/N]').upper().strip()[0]
    if escolha in 'SN':
        if escolha == 'S':
            formatar = True
            while True:
                escolha_moeda = input('Digite um 1 para R$ ou 2 para $: ')
                if escolha_moeda.isnumeric():
                    if escolha_moeda == '1' or escolha_moeda == '2':
                        break
            break
        else:
            escolha_moeda = ''
            formatar = False
            break
    else:
        print('<<<<< Escolha Incorreta!!! Tente Novamente!!! >>>>>')


print(f'O valor {moeda109.formatando_moeda(n, escolha_moeda, formatar)} com o aumento de 10% é igual a {moeda109.formatando_moeda(moeda109.aumentar(n, 0.10), escolha_moeda, formatar)}.')
print(f'O valor {moeda109.formatando_moeda(n, escolha_moeda, formatar)} com o desconto de 10% é igual a {moeda109.formatando_moeda(moeda109.diminuir(n, 0.10), escolha_moeda, formatar)}.')
print(f'O dobro do valor {moeda109.formatando_moeda(n, escolha_moeda, formatar)} é igual a {moeda109.formatando_moeda(moeda109.dobro(n), escolha_moeda, formatar)}.')
print(f'A metade do valor {moeda109.formatando_moeda(n, escolha_moeda, formatar)} é igual a {moeda109.formatando_moeda(moeda109.metade(n), escolha_moeda, formatar)}.')