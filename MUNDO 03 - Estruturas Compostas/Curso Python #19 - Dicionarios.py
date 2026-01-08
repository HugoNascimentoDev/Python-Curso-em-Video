
pessoas = {}
print(pessoas)

pessoas['nome'] = 'Hugo'
print(pessoas)

pessoas['idade'] = 35
print(pessoas)

pessoas['sexo'] = 'M'
print(pessoas)

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k.upper()} = {v}')
print(f'A pessoa {pessoas["nome"].upper()} tem {pessoas["idade"]} anos.')

brasil = []
estado1 = {'uf': 'Pernambuco', 'sigla': 'PE'}
estado2 = {'uf': 'Bahia', 'sigla': 'BA'}
print(brasil)
print(estado1)
print(estado2)

brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print(brasil[0])
print(brasil[1])

print(brasil[0]['uf'])
print(brasil[1]['uf'])



estados = {}
brasil = []
for c in range(0, 3):
    estados['uf'] = str(input('Digite o nome do estado: '))
    estados['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estados.copy())

print(estados)
print(brasil)

for estado in brasil:
    for k, v in estados.items():
        print(f'{k.upper()} = {v}')
        print(f'{"=" * 10}')
