with open("teste2.txt", "w+") as arquivo:
    arquivo.write("Ola, mundo ;D \n")
    arquivo.write("Bem-vindo ao Python.")

    arquivo.seek(0)

    conteudo = arquivo.read()
    print(conteudo)

precos = [200, 100, 300, 500, 400, 600]
with open("teste2.txt", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')