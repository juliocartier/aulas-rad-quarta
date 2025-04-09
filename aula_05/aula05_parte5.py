try:
    with open("texto_.txt", "r") as arquivo:
        arquivo_ler = arquivo.read()
        print(arquivo_ler)
except FileNotFoundError:
    print("Arquivo nao existe na pasta")