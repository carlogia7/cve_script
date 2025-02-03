# Auto CVEs

## Iniciando o projeto

### Opção 1: Docker

1. **Instale o Docker**:
   - Certifique-se de que o Docker está instalado em sua máquina. Você pode verificar isso executando `docker --version` no terminal.

2. **Inicie o Docker**:
   - No diretório do projeto, execute o seguinte comando para "buildar" o container:
     ```bash
     docker build -t cves_consulta .
     ```
   - O comando irá criar o contêineres, agora execute `docker run -d --name cves_consulta cves_consulta` para iniciar o projeto.

4. **Acesse o servidor**:
   - Abra o navegador e acesse o servidor em: [http://localhost:8000](http://localhost:8000)

---

### Opção 2: Ambiente Virtual (venv)

Se preferir configurar o ambiente localmente, siga os passos abaixo para usar o ambiente virtual:

1. **Instale o Python**:
   - Certifique-se de que o Python está instalado em sua máquina. Você pode verificar isso executando `python --version` no terminal.

2. **Entre no diretório do projeto**:
   - Navegue até o diretório correto:

3. **Crie um ambiente virtual (venv)**:
   - Caso ainda não tenha um ambiente virtual, crie um com o comando:
     ```bash
     python -m venv venv
     ```

4. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

5. **Instale os requerimentos**:
   - Baixe as dependências necessárias executando:
     ```bash
     pip install -r requirements.txt
     ```

7. **Inicie**:
   - Para rodar o servidor de desenvolvimento, use:
     ```bash
     python main.py
     ```
## Excel

### Como Formatar e Visualizar um Arquivo CSV no Excel

Este guia explica como importar, visualizar e formatar corretamente um arquivo `.csv` no Microsoft Excel.

## Passo 1: Verifique a Codificação do Arquivo
Certifique-se de que o arquivo `.csv` está salvo em uma codificação compatível com o Excel, como **UTF-8**. Para verificar:
- Abra o arquivo em um editor de texto como **Notepad++** ou **Visual Studio Code**.
- Verifique e altere a codificação se necessário.

## Passo 2: Abra o Excel
1. Abra o **Microsoft Excel**.
2. Acesse a aba **"Dados"**.

## Passo 3: Importar o Arquivo CSV
1. Clique em **"Obter Dados"**.
2. Selecione **"De Arquivo"** e depois **"De Texto/CSV"**.
3. Navegue até o local onde o arquivo `.csv` está salvo e selecione-o.

## Passo 4: Configurar a Importação
1. O Excel abrirá uma pré-visualização do arquivo.
2. Verifique se os dados estão sendo lidos corretamente.
3. Se necessário, ajuste o **delimitador** (o padrão é **vírgula (,)**, mas pode variar dependendo do formato do arquivo).
4. Clique em **"Carregar"** para importar os dados para uma nova planilha.

## Passo 5: Ajustar a Formatação
1. Ajuste a largura das colunas para que todo o texto fique visível:
   - Selecione todas as colunas e clique duas vezes na borda direita de qualquer cabeçalho de coluna.
2. Se necessário, ative a opção **"Quebra de Texto"** para ajustar o conteúdo dentro das células.

---

