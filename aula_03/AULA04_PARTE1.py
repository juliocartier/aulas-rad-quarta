arquivo = open("arquivo.txt")
print("Arquivo aberto", arquivo)
print(arquivo.name)
print(arquivo.mode)
print(arquivo.closed)

print(arquivo.read())
print(arquivo.seek(0))
print(arquivo.read(8))