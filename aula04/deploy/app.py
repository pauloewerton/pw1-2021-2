from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/questao01')
def imprimir_nome():
    return '<h1>Paulo Ewerton</h1>';

@app.route('/questao02')
def resolver_equacao():
    a = 3
    b = 5
    equacao = 2 * a * 3 * b
    return str(equacao);

@app.route('/questao07', methods=['POST'])
def somar_inteiros():
    num1 = request.form['num1']
    num2 = request.form['num2']
    soma = int(num1) + int(num2)
    return f'<h1>A soma é {soma}</h1>'
