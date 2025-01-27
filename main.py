import requests

def scan_cve(cve_id):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"

    response = requests.get(url)

    if response.status_code == 200:
        # Resposta em JSON
        cve_data = response.json()
        vulnerabilities = cve_data.get('vulnerabilities', [])

        print(f"{cve_data}\n\n")
        for vulnerability in vulnerabilities:
            cve_id = vulnerability['cve']['id']
            published_date, _ = vulnerability['cve']['published'].split("T", 1)
            descriptions = vulnerability['cve']['descriptions']
            # severity = vulnerability['cve']['metrics']['cvssMetricV31'][0]['cvssData']['baseSeverity']
            english_desc = next((desc['value'] for desc in descriptions if desc['lang'] == 'en'), None)

            print(f"CVE ID: {cve_id}")
            print(f"Published Date: {published_date}")
            # print(f"Severity: {severity}")
            print(f"Description: {english_desc if english_desc else 'No description available'}")
    else:
        print(f"Erro ao acessar a API: {response.status_code}, {response.text}")

if __name__ == "__main__":
    cve_id = "CVE-2024-23924"
    scan_cve(cve_id)