from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.json

    if 'valor' not in dados or 'valor2' not in dados or 'operacao' not in dados:
        return jsonify({'mensagem': 'Dados incompletos'}), 400

    valor1 = dados['valor']
    valor2 = dados['valor2']
    operacao = dados['operacao']

    if operacao == 'adicao':
        resultado = valor1 + valor2
    elif operacao == 'subtracao':
        resultado = valor1 - valor2
    elif operacao == 'multiplicacao':
        resultado = valor1 * valor2
    elif operacao == 'divisao':
        if valor2 == 0:
            return jsonify({'mensagem': 'Divisão por zero não é permitida'}), 400
        resultado = valor1 / valor2
    else:
        return jsonify({'mensagem': 'Operação não suportada'}), 400

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)