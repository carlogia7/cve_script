import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re

def submit():
    if quantidade.get() == 'unica':
        cve_valor = cve.get()
        # Captura apenas a primeira caso tenha mais
        cve_final = cve_valor.split()[0]
        if validar_cve(cve_final):
            print(f'CVE inserida: {cve_final}')
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira uma CVE válida.\nExemplo: CVE-2021-5678")
    # if quantidade.get() == 'multipla':
        
def file_input():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        file_label.config(text=f"Arquivo selecionado: {filename.split('/')[-1]}")

def validar_cve(cve):
    cve_regex = r'^CVE-\d{4}-\d{4,5}$'
    return re.match(cve_regex, cve) is not None

root = tk.Tk()
root.title('CVEs info')
root.geometry('500x600+50+50')
root.minsize(300, 400)
root.iconbitmap('assets/CVE_icon.ico')

# Variáveis
quantidade = tk.StringVar(value='unica')
cve = tk.StringVar()
filename = ""

# Layout
ttk.Label(root, text='Seleciona uma das opções:', font=('Arial', 14)).pack(pady=10)

# Radio modo único
ttk.Radiobutton(root, text='Consulta única', value='unica', variable=quantidade).pack(anchor='w', padx=20)
ttk.Entry(root, textvariable=cve, width=30).pack(pady=5, padx=20)

# Radio Arquivo
ttk.Radiobutton(root, text='Arquivo', value='multipla', variable=quantidade).pack(anchor='w', padx=20)
ttk.Button(root, text='Inserir arquivo (.txt)', command=file_input).pack(pady=5, padx=20)

# Label para mostrar arquivo selecionado
file_label = ttk.Label(root, text='Nenhum arquivo selecionado', font=('Arial', 12))
file_label.pack(pady=10)

# Enviar
ttk.Button(root, text="Enviar", command=submit).pack(pady=20)

root.mainloop()