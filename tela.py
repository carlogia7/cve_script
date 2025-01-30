import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re
from main import scan_cve

def submit():
    if quantidade.get() == 'unica':
        cve_valor = cve.get().strip()
        # Captura apenas a primeira caso tenha mais
        cve_final = [cve_valor.split()[0]]

        if validar_cve(cve_final):
            print(f'CVE válida inserida: {cve_final}')
            scan_cve(cve_final)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira uma CVE válida.\nExemplo: CVE-2021-5678")
    elif quantidade.get() == 'multipla':
        if not filename:
            messagebox.showerror("Arquivo não selecionado", "Por favor, selecione um arquivo para processar.") 
            return
        try:
            linhas = read_file(filename)
            cves_validas = validar_cve(linhas)
            if cves_validas:
                print(f"CVEs válidas no arquivo: {cves_validas}")
                scan_cve(cves_validas)
            else:
                messagebox.showwarning("Nenhuma CVE válida", "O arquivo não contém CVEs válidas.")
        except Exception as e:
            messagebox.showerror("Erro ao ler arquivo", f"Ocorreu um erro ao processar o arquivo: {e}")

def file_input():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
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