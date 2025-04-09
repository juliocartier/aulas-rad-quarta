def verificar_idade(idade):
    if idade >= 0 and idade < 18:
        raise ValueError("Idade minima e 18 anos")
    elif idade < 0:
        raise ValueError("A idade tem que ser um numero positivo")
    return "Acesso permitido"

try:
    idade = int(input("Digite a sua idade: "))
    print(verificar_idade(idade))
except ValueError as e:
    print(f"Erro: {e}")