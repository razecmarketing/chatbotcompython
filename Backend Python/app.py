import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Função que gera a resposta do chatbot com base na mensagem do usuário
def chatbot_response(user_message):
    time.sleep(1)  # Simula o tempo de resposta do chatbot

    if user_message.lower() == 'tchau':
        return "Ah, já vai? Foi bom conversar com você! Até mais! 👋"

    respostas = {
        "qual o seu nome?": "Eu sou o Robo Mais Mala do Mundo, e sou muito mal-humorado, hahaha! 😎",
        "como você está?": "Estou sempre em modo de energia máxima! Não sei o que é descanso! ⚡",
        "o que você faz?": "Eu sou o especialista em ser mala, e adoraria contar mais sobre mim, mas não posso. 🤖",
    }

    for pergunta, resposta in respostas.items():
        if pergunta in user_message.lower():
            return resposta

    return "Hmm, interessante! Vou pensar sobre isso... 💭"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_response = chatbot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
