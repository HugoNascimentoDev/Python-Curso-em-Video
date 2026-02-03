def mostrarlinha():
    print('=' * 27)

mostrarlinha()
print('     SISTEMA DE ALUNOS       ')
mostrarlinha()


def linha():
    print('-'*30)

#programa principal

linha()
print(f'{'HUGO BRITO':^30}')
linha()

#função mensagem criada com parametro onde msg é o parametro
def mensagem(msg):
    print('='*30)
    print(msg)
    print('='*30)

# a função mensagem recebe um valor para o parametro msg
mensagem(f'{'HUGO BRITO':^30}')
mensagem(f'{'APRENDENDO PYTHON':^30}')
mensagem(f'{'#DEV2026':^30}')

def soma(a, b):
    s = a + b
    print(f'Resultado: {s}\n')

def multiplacao(a, b):
    s = a * b
    print(f'Resultado: {s}\n')

def subtracao(a, b):
    s = a - b
    print(f'Resultado: {s}\n')

linha()
soma(5, 10)
linha()
subtracao(10, 5)
linha()
multiplacao(10, 10)
linha()
print() 

def contador(* num):
    for valor in num:
        print(valor, end =' ')
    print('FIM !!! ')
print('EMPACOTAMENTO')
linha()
contador(5, 7, 3, 0, 1, 4)
linha()
contador(8, 4, 7)
linha()



#fazendo com lista
linha()
valores = [7, 5, 7, 3, 8, 9, 1, 0]
print(valores)
linha()

def dobra(lista):
    pos = 0
    while pos <len (lista):
        lista[pos] *= 2
        pos += 1

dobra(valores)
linha()
print(valores)
linha()

def somando (* val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}!')

linha()
somando(5, 7, 8, 9, 5, 3)
linha()
somando(10, 20, 30)
linha()

def super_funcao(nome, *args, **kwargs):
    print(f"Nome: {nome}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

super_funcao("Lucas", 1, 2, 3, cidade="SP", status="Ativo")