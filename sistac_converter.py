import os

# Diretórios
entrada_dir = "entradas"
saida_dir = "saidas"

# Cria o diretório de saída se não existir
os.makedirs(saida_dir, exist_ok=True)

# Processa todos os arquivos .txt no diretório de entrada
for nome_arquivo in os.listdir(entrada_dir):
    if nome_arquivo.endswith(".txt"):
        caminho_entrada = os.path.join(entrada_dir, nome_arquivo)
        caminho_saida = os.path.join(saida_dir, nome_arquivo)

        with open(caminho_entrada, "r", encoding="utf-8") as entrada, \
             open(caminho_saida, "w", encoding="utf-8") as saida:

            for linha in entrada:
                campos = linha.strip().split(";")

                if campos[0] == "0":
                    # Linha da instituição, mantém como está
                    saida.write(linha)
                elif len(campos) >= 9:
                    # Extrai os campos necessários
                    numero = campos[0]
                    nome = campos[1]
                    cpf = campos[8]
                    data_nascimento = campos[3]

                    nova_linha = f"{numero};{nome};{cpf};{data_nascimento};\n"
                    saida.write(nova_linha)
                else:
                    print(f"⚠️ Linha ignorada no arquivo {nome_arquivo} (campos insuficientes): {linha.strip()}")

print("✅ Todos os arquivos foram processados com sucesso.")
