from flask import Flask, render_template 
import sqlite3 

# Inicializa o aplicativo Flask 
app = Flask(__name__) 
  

# Define a rota para a página que irá mostrar a lista de Digimons 
@app.route('/')
def digimon_list(): 

    # Conecta ao banco de dados SQLite 
    conn = sqlite3.connect('digimons.db')
    c = conn.cursor() 

    # Seleciona todos os Digimons cadastrados no banco de dados 
    c.execute("SELECT id, nome FROM digimons")
    digimons = c.fetchall() 

    # Renderiza o template HTML para exibir a lista de Digimons 
    return render_template('digimon_list.html', digimons=digimons)

  

# Executa o aplicativo Flask 
if __name__ == '__main__':
    app.run(port=8085)