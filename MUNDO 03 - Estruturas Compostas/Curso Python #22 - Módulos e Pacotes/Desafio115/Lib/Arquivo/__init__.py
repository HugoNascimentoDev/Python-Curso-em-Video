from Lib.Interface import *

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def CriarArquivo(nome):
    try:
        a = open(r'C:\Users\hugoh\OneDrive\Área de Trabalho\MUNDO DEV\GIT\Python-Curso-em-Video\MUNDO 03 - Estruturas Compostas\Curso Python #22 - Módulos e Pacotes\Desafio115\Lib\Arquivo\\' + nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def LerArquivo(nome):
    try:
        a = open(r'C:\Users\hugoh\OneDrive\Área de Trabalho\MUNDO DEV\GIT\Python-Curso-em-Video\MUNDO 03 - Estruturas Compostas\Curso Python #22 - Módulos e Pacotes\Desafio115\Lib\Arquivo\\' + nome, 'rt')
    except:
        print(erro('<<< ERRO >>> ao ler o arquivo!'))

    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(' - ')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
    finally:
        a.close()



def NovoCadastro(arquivo, nome = 'DESCONHECIDO', idade = '0'):
    try:
        a = open(r'C:\Users\hugoh\OneDrive\Área de Trabalho\MUNDO DEV\GIT\Python-Curso-em-Video\MUNDO 03 - Estruturas Compostas\Curso Python #22 - Módulos e Pacotes\Desafio115\Lib\Arquivo\\' + arquivo, 'at')
    except:
        print(erro('<<< ERRO >>> ao abrir o arquivo!'))
    else:
        try:
            a.write(f'{nome} - {idade}\n')
        except:
            print(erro('<<< ERRO >>> ao tentar escrever os dados!'))
        else:
            print(f'Novo registro de {nome} adicionado com SUCESSO!')
            a.close()
