print("Hello World")

frase = "a Python para análise de dados para dados"
# print(frase[1])
# print(frase[5])
# print(frase[0:10])
# print(frase[:5])
# print(frase[3:5])
x = frase.count("dados")
y = frase.count("pandas")
print(y)

#Converter primeira letra para maiusculo
print(frase.capitalize())

#Converter toda a frase para maiusculo
print(frase.upper())

z = frase.replace("Python", "Pandas")
print(z)