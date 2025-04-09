try:
    numero = int(input("Digite um numero: "))
    resultado = 20/numero
except ValueError:
    print("Erro: Deve ser digitado um numero inteiro")
except ZeroDivisionError:
    print("Erro: O numero da divisao e igual a 0, digite um numero diferente de 0")
except Exception as erro:
    print(f"Erro inesperado {erro}")
