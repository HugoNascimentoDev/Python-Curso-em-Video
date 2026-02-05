# DOCSTRING

def contador (i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end = ' -> ')
        c += p
    print('<<< FIM >>>')

contador(5, 50, 5)

help(contador)


# PARÂMETRO OU ARGUMENTO OPCIONAL

def somar (a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'RESULTADO: {s}')
    

somar(5, 8)
somar(7, 8, 9)
somar()

def saudacao (nome = 'amigo'):
    print(f'Olá, {nome}!')

saudacao('Hugo')
saudacao('Brenda')
saudacao()

# ESCOPO DE VARIÁVEL

def teste(b):
    b += 4
    c = 10
    print(f'A vale dentro {a}.')
    print(f'B vale dentro {b}')
    print(f'C vale dentro {c}')


a = 15
teste(a)

print(f'A fora vale {a}')

# RETONANDO VALORES (RETURN)

def somar2 ( a= 0, b=0, c=0):
    resultado = a + b + c
    return resultado
r1 = somar2(10, 20, 30)
r2 = somar2(7, 8, 9)
r3 = somar2(5, 8)

print(f'Minhas somas foram iguais a... {r1}, {r2}, {r3}!')


def fatorial (num = 1):
    f = 1
    for c in range (num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


f1 = fatorial(10)
f2 = fatorial(5)
f3 = fatorial(3)

print(f'''RESULTADO FATORIAL: 
F1 = {f1}
F2 = {f2}
F3 = {f3}''')


def par (num = 0):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))

print(F'O número é PAR???? {par(num)}')