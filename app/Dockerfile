# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie todo o conteúdo do diretório local para o diretório de trabalho no contêiner
COPY . .

# Comando padrão para executar o aplicativo FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
