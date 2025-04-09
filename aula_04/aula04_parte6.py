import os

try:
    os.remove("texto_.txt")
    print("Arquivo removido com sucesso")
except FileNotFoundError as error:
    print("Arquivo nao existe")
    print("descricao do nosso erro ", error)