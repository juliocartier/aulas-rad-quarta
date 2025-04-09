with open("arquivo_rad04.txt", "r") as arquivo:
    print("Representacao original da linha")
    for linha in arquivo:
        dado_da_linha = linha.strip()
        # print(repr(linha))
        # print(repr(dado_da_linha))


lista_de_comida = ['Arroz', 'Feijao', 'Carne', 'Banana', 'Uva']
lista_ = ','.join(lista_de_comida)
with open('lista_de_comidas.txt', 'w') as arquivo:
    # for lista in lista_de_comida:
    arquivo.write(lista_)