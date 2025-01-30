import tkinter as tk
from tkinter import ttk
import requests, csv
from typing import List, Dict
from tkinter import messagebox

def scan_cve(cves_lista):
    for cve_id in cves_lista:
        URL_API = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
        # Realize a requisição GET, proxies poderá ser desabilitado no futuro
        try:
            response = requests.get(URL_API)
            if response.status_code == 200:
                # Converta a resposta em JSON
                cve_data = response.json()
                vulnerabilities = cve_data.get('vulnerabilities', [])

                if not vulnerabilities:
                    print(f"Nenhuma vulnerabilidade encontrada para o CVE: {cve_id}")
                    continue
                result_list = []
                # print(f"{cve_data}\n\n")
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
                    print(result_list)
                    write_csv(result_list, 'vulnerabilities.csv')
            else:
                print(f"Erro ao acessar a API: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Erro ao realizar a requisição: {e}")

def write_csv(data: List[Dict], filename: str):
    # Escreve os dados em um arquivo CSV.
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['cve_id', 'published_date', 'last_modified_date', 'description', 
                      'severity', 'base_score', 'source_identifier', 'cwes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            row['cwes'] = ", ".join(row['cwes'])
            writer.writerow(row)
    messagebox.showinfo("SUCESSO")

if __name__ == "__main__":
    cves_lista = ["CVE-2021-5678"]
    scan_cve(cves_lista)