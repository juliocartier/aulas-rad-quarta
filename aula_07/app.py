import tkinter as tk

def mostrar_nome():
    nome = entrada.get()
    print(f"Ola, {nome}")


janela = tk.Tk()
janela.title("Exemplo Tkinter")

tk.Label(janela, text="Digite o seu nome:").pack()
entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Enviar", command=mostrar_nome).pack()

janela.mainloop()
