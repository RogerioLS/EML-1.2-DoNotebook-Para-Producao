# Utiliza a imagem base Python versão 3.10.2-slim, uma versão mais leve do Python
FROM python:3.10.2-slim

# Define o diretório de trabalho dentro do contêiner como /app
WORKDIR /app

# Copia o arquivo requirements.txt do diretório local sources/app para o diretório de trabalho atual do contêiner
COPY sources/app/requirements.txt ./

# Copia o arquivo modelo_churn.pkl do diretório local sources/build_model para o diretório de trabalho atual do contêiner
COPY sources/build_model/modelo_churn.pkl ./

# Copia o arquivo app.py do diretório local sources/app para o diretório de trabalho atual do contêiner
COPY sources/app/app.py ./

# Executa o comando para instalar as dependências Python listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define o ponto de entrada do contêiner, que é o comando usado para iniciar a aplicação.
# Aqui, é configurado para iniciar a aplicação Flask usando o comando flask run
# O comando é configurado para escutar em todas as interfaces de rede dentro do contêiner na porta 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
