import tkinter as tk
from tkinter import messagebox
import pg8000
from datetime import datetime


conexao_banco = pg8000.connect(
    user="postgres",
    password="123456",
    host="localhost",
    database="aula_rad_quarta"
)

def inserir_empregado():
    try:
        matricula = int(entry_matricula.get())
        nome = entry_nome.get()
        data_nasc = datetime.strptime(entry_data.get(), "%Y-%m-%d").date()

        cursor = conexao_banco.cursor()
        cursor.execute(
            "INSERT INTO empregado (matricula, nome_empregado, data_nasc) VALUES (%s, %s, %s)",
            (matricula, nome, data_nasc)
            )
        conexao_banco.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Empregado cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

def mostrar_empregado():
    try:
        cursor = conexao_banco.cursor()
        cursor.execute("SELECT matricula, nome_empregado, data_nasc from empregado order by matricula")
        registros = cursor.fetchall()
        cursor.close()

        text_resultado.delete("1.0", tk.END)

        for emp in registros:
            linha = f"Matricula: {emp[0]}, Nome: {emp[1]}, Nascimento: {emp[2]}\n"
            text_resultado.insert(tk.END, linha)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar os dados {e}")


janela = tk.Tk()
janela.title("Cadastro de Empregado")

tk.Label(janela, text="Matricula").grid(row=0, column=0)
entry_matricula = tk.Entry(janela)
entry_matricula.grid(row=0, column=1)

tk.Label(janela, text="Nome").grid(row=1, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1)

tk.Label(janela, text="Data Nasc(YYYY-MM-DD)").grid(row=2, column=0)
entry_data = tk.Entry(janela)
entry_data.grid(row=2, column=1)

tk.Button(janela, text="Cadastrar", command=inserir_empregado).grid(row=3, column=0, pady=5)
tk.Button(janela, text="Listar Empregados", command=mostrar_empregado).grid(row=3, column=1)
# botao_enviar.grid(row=3, column=0, columnspan=2, pady=10)

text_resultado = tk.Text(janela, width=80, height=10)
text_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

janela.mainloop()

conexao_banco.close()