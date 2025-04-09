try:
    with open("dados_.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Arquivo lido com sucesso")
except FileNotFoundError:
    print("Erro: Arquivo nao encontrado")
else:
    print("Conteudo do arquivo", conteudo)
finally:
    print("Finalizado a leitura do arquivo")