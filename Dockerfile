# Imagem base mínima com Python 3.11
FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho dentro do container
WORKDIR /app

# Instala pacotes do sistema necessários para compilar firebase-admin e pandas
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requirements
COPY requirements-min-docker.txt .

# Instala as dependências via requirements
RUN pip install --no-cache-dir -r requirements-min-docker.txt

# Copia os arquivos principais necessários para execução
COPY src/water_scan_main.py ./src/water_scan_main.py
COPY src/best_rf_full.pkl ./src/best_rf_full.pkl

# # Copiar a chave do Firebase
COPY .env/serviceAccountKey.json .env/serviceAccountKey.json

# Entrypoint para executar o script principal
ENTRYPOINT ["python", "src/water_scan_main.py"]
