import os
import requests
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

CLIENT_ID = os.getenv("MELI_CLIENT_ID")
CLIENT_SECRET = os.getenv("MELI_CLIENT_SECRET")
REDIRECT_URI = os.getenv("MELI_REDIRECT_URI")
PORT = int(os.getenv("PORT", 3000))

@app.route("/", methods=["GET"])
def home():
    return "EbookBot do Mercado Livre (Python) está rodando com sucesso!"

@app.route("/auth", methods=["GET"])
def auth():
    auth_url = (
        f"https://auth.mercadolivre.com.br/authorization?"
        f"response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    )
    return redirect(auth_url)

@app.route("/callback", methods=["GET"])
def callback():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "Código não fornecido"}), 400

    url = "https://api.mercadolibre.com/oauth/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url, data=payload, headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
