idade = int(input("Qual é a sua idade?"))
if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")
    
altura = float(input("Qual é a sua altura?"))    
if altura < 1.8:
    print("Baixo")
elif altura > 1.8 and altura < 2.0:
    print("Alto")
else:
    print("Muito Alto")
    
def hello(nome):
    print("Ola", nome)

hello("Juliano")    