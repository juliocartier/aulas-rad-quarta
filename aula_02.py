print("Hello World")

### A DEFINICAO DA VARIAVEL INTEIRA SOMA
### RECEBE UMA SOMA DE DOIS NUMEROS
soma = 2 + 2
print(soma)
print(type(soma))

### A VARIAVEL SOMA AGORA VAI UMA STRING
soma = "2" + "2"
print(soma)
print(type(soma))

# CRIAR UMA FUNÇÃO 
# QUE REALIZA A SOMA DE DOIS NUMEROS 
# INTEIROS
def soma2(x, y):
    retorno = int(x) + int(y)
    return retorno

# CRIAR UMA FUNÇÃO 
# QUE REALIZA A SOMA DE DOIS NUMEROS 
# INTEIROS
def soma3(x, y):
    retorno = x + y
    return retorno

print(soma2(6, 7))
## REALIZA A SOMA DE DOIS NUMEROS,
# COMO TAMBÉM CONCATENAR AS STRING.
print(soma3("2", "2"))
print(soma3(2, 2))
print(soma2(2.5, 20.8))

