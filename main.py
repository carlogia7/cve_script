import tkinter as tk
from tkinter import ttk
import requests, csv, logging, os, time
from typing import List, Dict
from tkinter import messagebox
import tela

logging.basicConfig(level=logging.DEBUG)

def scan_cve(cves_lista: List[str], filename: str = 'vulnerabilities.csv'):
    result_list = []
    for index, cve_id in enumerate(cves_lista):
        URL_API = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
        # Realize a requisição GET, proxies poderá ser desabilitado no futuro

        # time sleep para respeitar o limite da API
        if index > 0 and len(cves_lista) > 5:
            time.sleep(5)
        try:
            response = requests.get(URL_API)
            if response.status_code == 200:
                # Converta a resposta em JSON
                cve_data = response.json()
                vulnerabilities = cve_data.get('vulnerabilities', [])

                if not vulnerabilities:
                    logging.warning(f"Nenhuma vulnerabilidade encontrada para o CVE: {cve_id}")
                    continue
                for vulnerability in vulnerabilities:
                    cve_info = vulnerability.get('cve', {})

                    cve_id = cve_info.get('id', 'N/A')

                    published_date, _ = cve_info.get('published', 'N/A').split("T", 1)
                    last_modif_date, _ = cve_info.get('lastModified', 'N/A').split("T", 1)

                    descriptions = cve_info.get('descriptions', [])
                    english_desc = next((desc['value'] for desc in descriptions if desc['lang'] == 'en'), 'No description available')

                    # Métricas CVSS
                    metrics = cve_info.get('metrics', {}).get('cvssMetricV31', [])
                    severity = 'N/A'
                    base_score = 'N/A'
                    if metrics:
                        primary_metric = metrics[0]
                        severity = primary_metric.get('cvssData', {}).get('baseSeverity', 'N/A')
                        base_score = primary_metric.get('cvssData', {}).get('baseScore', 'N/A')
                    
                    source_identifier = cve_info.get('sourceIdentifier', 'N/A')

                    # CWEs relacionadas
                    weaknesses = cve_info.get('weaknesses', [])
                    cwes = [weakness['description'][0]['value'] for weakness in weaknesses if 'description' in weakness and weakness['description']]

                    result_list.append({
                        'cve_id': cve_id,
                        'published_date': published_date,
                        'last_modified_date': last_modif_date,
                        'description': english_desc,
                        'severity': severity,
                        'base_score': base_score,
                        'source_identifier': source_identifier,
                        'cwes': cwes,
                    })
            else:
                logging.error(f"Erro ao acessar a API: {response.status_code}, {response.text}")
        except Exception as e:
            logging.error(f"Erro ao realizar a requisição: {e}")
    if result_list:
        write_csv(result_list, filename)

def write_csv(data: List[Dict], filename: str):

    file_exists = os.path.exists(filename)
    # Escreve os dados em um arquivo CSV.
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['cve_id', 'published_date', 'last_modified_date', 'description', 
                      'severity', 'base_score', 'source_identifier', 'cwes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for row in data:
            row['cwes'] = ", ".join(row['cwes'])
            writer.writerow(row)
    messagebox.showinfo("Sucesso", f"O arquivo {filename} foi criado e está disponível")

def submit(quantidade_valor, cve_valor, filename):
    if quantidade_valor == 'unica':
        # Captura apenas a primeira caso tenha mais
        cve_final = [cve_valor.strip().split()[0]]

        if tela.validar_cve(cve_final):
            logging.debug(f'CVE válida inserida: {cve_final}')
            scan_cve(cve_final)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, insira uma CVE válida.\nExemplo: CVE-2021-5678")
    elif quantidade_valor == 'multipla':
        if not filename:
            messagebox.showerror("Arquivo não selecionado", "Por favor, selecione um arquivo para processar.") 
            return
        try:
            linhas = tela.read_file(filename)
            cves_validas = tela.validar_cve(linhas)
            if cves_validas:
                logging.debug(f"CVEs válidas no arquivo: {cves_validas}")
                scan_cve(cves_validas)
            else:
                messagebox.showwarning("Nenhuma CVE válida", "O arquivo não contém CVEs válidas.")
        except Exception as e:
            messagebox.showerror("Erro ao ler arquivo", f"Ocorreu um erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    tela.inicia_tela()
