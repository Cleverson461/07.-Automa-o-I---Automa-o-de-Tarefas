import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title('Cadastro de Alunos')

# 1 - Função para Adicionar Estudante
def add_student():
    name = entry_name.get()
    email = entry_email.get()
    
    tree.insert('', tk.END, values=(name, email))
    
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# 2 - Criando Tabela TreeView
tree = ttk.Treeview(root, columns=('Name', 'Email'))
tree.heading('Name', text='Name')
tree.heading('Email', text='Email')
tree.pack()

# 3 - Criando campos Name e Email
# name
label_name = tk.Label(root, text='Name')
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

# email
label_email = tk.Label(root, text='Email')
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

button_add = tk.Button(root, text='Add', command=add_student)
button_add.pack()


root.mainloop()