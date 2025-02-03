import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re
from main import submit

def file_input(root, file_label):
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        root.filename_var.set(filename)
        file_label.config(text=f"Arquivo selecionado: {filename.split('/')[-1]}")
    else:
        file_label.config(text="Nenhum arquivo selecionado")

def validar_cve(cves):
    cve_pattern = re.compile(r'^CVE-\d{4}-\d{4,5}$')
    cves_validos = [cve for cve in cves if cve_pattern.match(cve)]
    return cves_validos

def read_file(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return lines


def inicia_tela():

    root = tk.Tk()
    root.title('CVEs info')
    root.geometry('500x600+50+50')
    root.minsize(300, 400)
    root.iconbitmap('assets/CVE_icon.ico')

    root.quantidade = tk.StringVar(value='unica')
    root.cve = tk.StringVar()
    root.filename_var = tk.StringVar(value="")

    def chamar_submit():
        submit(root.quantidade.get(), root.cve.get(), root.filename_var.get())

    # Layout
    ttk.Label(root, text='Seleciona uma das opções:', font=('Arial', 14)).pack(pady=10)

    # Radio modo único
    ttk.Radiobutton(root, text='Consulta única', value='unica', variable=root.quantidade).pack(anchor='w', padx=20)
    ttk.Entry(root, textvariable=root.cve, width=30).pack(pady=5, padx=20)

    # Radio Arquivo
    ttk.Radiobutton(root, text='Arquivo', value='multipla', variable=root.quantidade).pack(anchor='w', padx=20)
    ttk.Button(root, text='Inserir arquivo (.txt)', command=lambda: file_input(root, file_label)).pack(pady=5, padx=20)

    # Label para mostrar arquivo selecionado
    file_label = ttk.Label(root, text='Nenhum arquivo selecionado', font=('Arial', 12))
    file_label.pack(pady=10)

    # Enviar
    ttk.Button(root, text="Enviar", command=chamar_submit).pack(pady=20)

    root.mainloop()
