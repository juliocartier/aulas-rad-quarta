try:
    arquivo = open("dados1.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError as error:
    print(f"Erro: Arquivo nao encontrado {error}")
finally:
    print("O programa foi executado ate o final")