import numpy as np
import requests

# Função para gerar dados aleatórios baseados na estrutura conhecida
def generate_random_data():
    return [
        np.random.randint(0, 2),
        np.random.randint(0, 2),
        np.random.uniform(0, 20),
        np.random.randint(18, 61),
        np.random.uniform(0, 2),
        np.random.randint(0, 2),
        np.random.uniform(50, 100),
        np.random.randint(0, 11),
        np.random.randint(0, 2)
    ]

# URL do servidor de previsão
url = 'http://127.0.0.1:5000/predict'

# Número de requisições que você deseja enviar
num_requests = 10

# Enviando múltiplas requisições
for _ in range(num_requests):
    random_data = generate_random_data()
    data = {"features": random_data}
    response = requests.post(url, json=data)
    print("Data sent:", random_data)
    print("Response received:", response.json())

