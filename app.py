import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PORT = int(os.getenv("PORT", 3000))
CLIENT_ID = os.getenv("MELI_CLIENT_ID")
CLIENT_SECRET = os.getenv("MELI_CLIENT_SECRET")

@app.route('/')
def home():
    return 'EbookBot do Mercado Livre (Python) está rodando com sucesso!'

# Rota de callback do OAuth
@app.route('/get', methods=['GET'])
def oauth_callback():
    code = request.args.get('code')
    if code:
        return f'Authorization Code recebido com sucesso: {code}'
    return 'Endpoint de redirecionamento ativo.'

# Webhook para escutar as vendas/mensagens
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print('Notificação recebida do Mercado Livre:', data)
    return 'Webhook recebido', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)