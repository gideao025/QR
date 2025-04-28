# Usa a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos (se existir) ou instala diretamente
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Define o comando para rodar a aplicação
CMD ["python", "app.py"]