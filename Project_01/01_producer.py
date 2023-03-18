from kafka import KafkaProducer
from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

# Configurações do consumer
topic_name = 'digimons'
bootstrap_servers = ['localhost:9092']
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)


@app.route('/digimons', methods=['POST'])
def add_digimon():
    command = request.json.get('command')
    if command == 'begin_web_scraping':
        # Inicializa o driver do Firefox
        driver = webdriver.Firefox()

        # Abre a página dos digimons
        driver.get("https://pt.everybodywiki.com/Lista_de_esp%C3%A9cies_Digimon")

        # Achei o xpath que eu busquei na pagina (totally ad hoc)
        table_body = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[5]/div/div[2]/div[3]/div[1]/div/div[1]')

        # a pagina tem uma tabela separada por ordem afabetica, por isso chamei de 'alphabet'
        alphabet = table_body.find_elements(By.TAG_NAME, "ul")

        # cada linha é uma letra, e ignoro o começo e o fim, pq são menus
        for letter in alphabet[1:-1]:
            # a lista de digimons é uma lista simples com li
            digimon_list = letter.find_elements(By.TAG_NAME, "li")

            # se não for um espaço vazio. pego cada elemento
            for digimon in digimon_list:
                digimon_name = digimon.text
                if len(digimon_name) > 0:
                    producer.send(topic_name, value=digimon_name.encode('utf-8'))

        # Fecha o driver do Firefox
        driver.quit()
        return jsonify({'message': 'Todos os Digimons adicionado com sucesso!'})
    else:
        return jsonify({'message': 'FALHOU!'})


if __name__ == '__main__':
    app.run(port=7888)
