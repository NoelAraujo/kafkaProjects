import requests

# Defina a URL do endpoint do servidor REST
url = "http://localhost:7888/digimons"

# Defina o corpo da requisição em formato JSON
body = {
    "command": 'begin_web_scraping'
}

# Envie a requisição POST para o servidor REST
response = requests.post(url, json=body)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    print(f"Dados foram capturados")
else:
    print(f"Ocorreu um erro ao enviar o nome do Digimon para o servidor REST. Código de status: {response.status_code}")
