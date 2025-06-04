import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = 'http://127.0.0.1:5009/api'

class UsuarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Usuarios")
        self.root.geometry("600x400")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.tree = ttk.Treeview(self.frame, columns=("id", "email"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("email", text="Email")
        self.tree.pack()
        
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Listar Usuarios", command=self.listar_usuarios).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Criar Usuario", command=self.criar_usuarios).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Atualizar Email", command=self.atualizar_usuarios).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Deletar Usuario", command=self.deletar_usuarios).grid(row=0, column=3, padx=5)
        
        self.email_var = tk.StringVar()
        self.senha_var = tk.StringVar()
        self.novo_email_var = tk.StringVar()
        
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)
        
        tk.Label(entry_frame, text="Email: ").grid(row=0, column=0)
        tk.Entry(entry_frame, textvariable=self.email_var).grid(row=0, column=1)
        
        tk.Label(entry_frame, text="Senha: ").grid(row=1, column=0)
        tk.Entry(entry_frame, textvariable=self.senha_var).grid(row=1, column=1)
        
        tk.Label(entry_frame, text="Novo Email (atualizar): ").grid(row=2, column=0)
        tk.Entry(entry_frame, textvariable=self.novo_email_var).grid(row=2, column=1)
        
    def listar_usuarios(self):
        try:
            response = requests.get(f"{API_URL}/lista_usuarios")
            if response.status_code == 200:
                self.tree.delete(*self.tree.get_children())
                for usuarios in response.json():
                    self.tree.insert("","end", values=(usuarios["id"], usuarios["email"]))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisição: {e}")
            
    def criar_usuarios(self):
        email = self.email_var.get()
        senha = self.senha_var.get()
        
        if not email or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return
        
        payload = {"email": email, "password": senha}
        try:
            response = requests.post(f"{API_URL}/criar_usuarios", json=payload)
            if response.status_code == 201:
                messagebox.showinfo("Sucesso", "Usuario Criado")
            else:
                messagebox.showerror("Erro", response.json())
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisição ao criar o usuario {e}")
            
    def deletar_usuarios(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione um usuario antes de deletar")
            return
        
        user_id =self.tree.item(selected_item[0])["values"][0]
        try:
            response = requests.delete(f"{API_URL}/deletar_usuarios/{user_id}")
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Usuario deletado")
            else:
                messagebox.showerror("Erro", "Erro ao deletaro usuario")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisição de deletar o usuario: {e}")
            
    def atualizar_usuarios(self):
        selected_item = self.tree.selection()
        novo_email = self.novo_email_var.get()
        if not selected_item or not novo_email:
            messagebox.showwarning("Aviso", "Selecione um usuario e como também o campo de email para ser digitado.")
            return
        
        user_id = self.tree.item(selected_item[0])["values"][0]
        payload = {"email": novo_email}
        
        try:
            response = requests.put(f"{API_URL}/atualizar_usuarios/{user_id}", json=payload)
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Email atualizado")
            else:
                messagebox.showerror("Erro", "Erro ao atualizar o usuario")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na requisição {e}")
            
            
        
if __name__ == "__main__":
    root = tk.Tk()
    app = UsuarioApp(root)
    root.mainloop()