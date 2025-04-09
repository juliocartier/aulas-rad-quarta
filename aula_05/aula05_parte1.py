try:
    resultado = 20/0
    print(resultado)
except ZeroDivisionError as erro:
    print("Erro: Nao e possivel realizar a divisao por 0", erro)