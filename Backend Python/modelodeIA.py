import time

# Função que gera a resposta do chatbot com base na mensagem do usuário
def chatbot_response(user_message):
    time.sleep(1)  # Simula o tempo de resposta do chatbot

    # Se o usuário digitar "tchau", encerra a conversa
    if user_message.lower() == 'tchau':
        return "Ah, já vai? Foi bom conversar com você! Até mais! 👋"

    # Respostas simples baseadas nas mensagens do usuário
    respostas = {
        "qual o seu nome?": "Eu sou o Robo Mais Mala do Mundo, e sou muito mal-humorado, hahaha! 😎",
        "como você está?": "Estou sempre em modo de energia máxima! Não sei o que é descanso! ⚡",
        "o que você faz?": "Eu sou o especialista em ser mala, e adoraria contar mais sobre mim, mas não posso. 🤖",
    }

    # Se o chatbot reconhecer uma pergunta específica, responde com base no dicionário
    for pergunta, resposta in respostas.items():
        if pergunta in user_message.lower():
            return resposta

    # Se o chatbot não reconheceu a pergunta, gera uma resposta padrão
    return "Hmm, interessante! Vou pensar sobre isso... 💭"

# Função principal para interação com o chatbot
def chatbot():
    print("Olá! Vamos bater um papo?\n")
    time.sleep(1)

    nome = input("Qual é o seu nome? ")
    print(f"\nHaha, {nome} é um nome muito bonito!\nJá pensei em chamar meu próximo robozinho assim. 🤖\n")
    time.sleep(1)

    idade = input("Quantos anos você tem? ")
    print(f"\n{idade} anos? Tá na flor da idade, hein?! 😂\nAproveita, porque o tempo voa mais rápido que uma nave espacial! 🚀\n")
    time.sleep(1)

    peso = input("Quanto você pesa? ")
    print(f"\nHmm... {peso} kg? O que? Já pensou em emagrecer?, tá doido viu!\nO importante é ter saúde mesmo! 😆\n")
    time.sleep(1)

    print(f"\nMuito prazer em te conhecer, {nome}! Vamos continuar nosso papo!\n")
    time.sleep(1)

    perguntas = [
        "Se você pudesse viajar para qualquer lugar agora, para onde iria?",
        "Qual foi a coisa mais engraçada que aconteceu com você recentemente?",
        "Se tivesse que escolher um superpoder, qual seria?",
    ]

    comentarios_divertidos = [
        "\nHaha, boa escolha! Já tô imaginando a cena! 😆\n",
        "\nCaramba, essa foi inesperada! Adorei! 🤣\n",
        "\nMuito criativo! Você tem uma mente brilhante! 🧠✨\n",
    ]

    for i in range(len(perguntas)):
        resposta = input(f"{perguntas[i]}\n> ")

        if "tchau" in resposta.lower():
            print("\nAh, já vai? Foi bom conversar com você! Até mais! 👋\n")
            break

        print(comentarios_divertidos[i])
        time.sleep(1)

    print("\nAdorei nosso papo! Vamos continuar outro dia.\nAté mais! 🚀\n")

# Inicia o chatbot se o script for executado
if __name__ == "__main__":
    chatbot()
