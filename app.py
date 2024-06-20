from flask import Flask, jsonify, render_template
import random
import os

app = Flask(__name__)

def gerar_numeros(qtd_numeros, min_valor, max_valor):
    return sorted(random.sample(range(min_valor, max_valor + 1), qtd_numeros))

@app.route('/api/gerar_numeros_loteria1')
def gerar_numeros_loteria1():
    qtd_numeros = 6
    min_valor = 1
    max_valor = 60
    numeros = gerar_numeros(qtd_numeros, min_valor, max_valor)
    return jsonify(numeros)

@app.route('/api/gerar_numeros_loteria2')
def gerar_numeros_loteria2():
    qtd_numeros = 15
    min_valor = 1
    max_valor = 25
    numeros = gerar_numeros(qtd_numeros, min_valor, max_valor)
    return jsonify(numeros)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

