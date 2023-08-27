from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando uma base de dados temporária para perguntas e respostas
perguntas = []
respostas = []

# Função auxiliar para obter o próximo ID disponível
def get_next_id(lista):
    if not lista:
        return 1
    return max(item['id'] for item in lista) + 1

# Endpoints GET

@app.route('/perguntas', methods=['GET'])
def get_perguntas():
    return jsonify(perguntas)

@app.route('/perguntas/<int:id>', methods=['GET'])
def get_pergunta(id):
    pergunta = next((p for p in perguntas if p['id'] == id), None)
    if pergunta:
        return jsonify(pergunta)
    return jsonify({'message': 'Pergunta não encontrada'}), 404

@app.route('/respostas', methods=['GET'])
def get_respostas():
    return jsonify(respostas)

@app.route('/respostas/<int:id>', methods=['GET'])
def get_resposta(id):
    resposta = next((r for r in respostas if r['id'] == id), None)
    if resposta:
        return jsonify(resposta)
    return jsonify({'message': 'Resposta não encontrada'}), 404

# Endpoints POST

@app.route('/perguntas', methods=['POST'])
def cadastrar_pergunta():
    data = request.get_json()
    pergunta = {
        'id': get_next_id(perguntas),
        'pergunta': data['pergunta']
    }
    perguntas.append(pergunta)
    return jsonify({'id': pergunta['id']}), 201

@app.route('/respostas', methods=['POST'])
def cadastrar_resposta():
    data = request.get_json()
    resposta = {
        'id': get_next_id(respostas),
        'resposta': data['resposta'],
        'id_pergunta': data['id_pergunta']
    }
    respostas.append(resposta)
    return jsonify({'id': resposta['id']}), 201

# Endpoints DELETE

@app.route('/perguntas/<int:id>', methods=['DELETE'])
def deletar_pergunta(id):
    pergunta = next((p for p in perguntas if p['id'] == id), None)
    if pergunta:
        perguntas.remove(pergunta)
        return jsonify({'message': 'Pergunta deletada com sucesso'})
    return jsonify({'message': 'Pergunta não encontrada'}), 404

@app.route('/respostas/<int:id>', methods=['DELETE'])
def deletar_resposta(id):
    resposta = next((r for r in respostas if r['id'] == id), None)
    if resposta:
        respostas.remove(resposta)
        return jsonify({'message': 'Resposta deletada com sucesso'})
    return jsonify({'message': 'Resposta não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
