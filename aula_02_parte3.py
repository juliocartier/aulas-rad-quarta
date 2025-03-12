vetores_de_dados = [1, 4, 4, 8, 9, 21, 2]

for dado in vetores_de_dados:
    if dado == 8:    
        print(dado)

print("Outro for")
for dado in range(len(vetores_de_dados)):
    print(dado)
    if dado == 5:
        print(vetores_de_dados[dado])
