from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Calcular(Resource):
    def post(self):
        """
        Realiza operações matemáticas com os valores fornecidos.
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                valor:
                  type: integer
                valor2:
                  type: integer
                operacao:
                  type: string
                  enum: ['adicao', 'subtracao', 'multiplicacao', 'divisao']
        responses:
          200:
            description: Resultado da operação
            schema:
              type: object
              properties:
                resultado:
                  type: number
          400:
            description: Erro na requisição
            schema:
              type: object
              properties:
                mensagem:
                  type: string
        """
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

api.add_resource(Calcular, '/calcular')

if __name__ == '__main__':
    app.run(debug=True)