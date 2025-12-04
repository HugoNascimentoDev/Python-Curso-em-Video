import os

# 1. Barra invertida no caminho (\)
# No Python, a barra invertida \ é interpretada como caractere de escape (por exemplo, \n vira quebra de linha). Por isso, seu caminho "C:\Users\hugoh\OneDrive\Área de Trabalho\..." pode dar erro.
# ✅ Soluções possíveis:
# Usar string raw com r"":

# pasta onde os arquivos serão criados
pasta_destino = r"C:\Users\hugoh\OneDrive\Área de Trabalho\MUNDO DEV\GIT\Python-Curso-em-Video\MUNDO 03 - Estruturas Compostas"


# cria a pasta se não existir
os.makedirs(pasta_destino, exist_ok=True)

# gera os arquivos de 1 até 40
for i in range(1, 115):
    nome_arquivo = f"Desafio {i:02}.py"  # :02 garante dois dígitos (01, 02, ..., 40)
    caminho = os.path.join(pasta_destino, nome_arquivo)
    
    # cria o arquivo vazio ou com conteúdo inicial
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(f"# Arquivo {nome_arquivo}\n")
        f.write("# Seu código aqui\n")

print("Arquivos gerados com sucesso!")