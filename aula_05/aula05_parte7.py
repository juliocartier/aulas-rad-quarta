try:
    with open("arquivo_leitura.txt", "w") as arquivo:
        # arquivo_ler = arquivo.read()
        # print(arquivo_ler)
        arquivo.write("Teste")
except PermissionError:
    print("Erro: voce nao tem a permissao para alterar esse arquivo, voce so tem permissao para ler")