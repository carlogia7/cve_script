FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["py", "main.py"]

# docker build -t cves_consulta .
# docker run -d --name cves_consulta cves_consulta