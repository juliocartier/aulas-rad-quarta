try:
    arquivo = open("novo_arquivo.txt", "w")
    arquivo.write("Escrevendo algum texto no nosso arquivo")
    print("Arquivo criado com sucesso")
except Exception as erro:
    print(f"Erro ao manipular o arquivo: {erro}")
finally:
    arquivo.close()
    print("Arquivo fechado")