precos = [1000, 2000, 100, 200, 400]

with open("precos_roupas.txt", 'a') as arquivo:
    for preco in precos:
        arquivo.write(str(preco)+ '\n')
        print(preco)
    arquivo.write('60000' + '\n')

precos = [2000, 1000]
with open("precos_roupas.txt", 'w') as arquivo:
    for preco in precos:
        arquivo.write(str(preco)+ '\n')
