disciplinas = ["1. RAD\n", "2. Introducao a C\n", "3. POO\n"]

with open("disciplinas.txt", "w") as arquivo:
    arquivo.write("Relacao das Disciplinas do curso \n")
    arquivo.writelines(disciplinas)


with open("disciplinas.txt", "r") as arquivo:
    print(arquivo.read())
