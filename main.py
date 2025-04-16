from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint que o SGP vai chamar
@app.route('/send', methods=['POST'])
def sgp_gateway():
    try:
        # Pega o token do JSON enviado pelo SGP
        sgp_token = request.args.get("token") or request.headers.get("x-sgp-token")

        if not sgp_token:
            return jsonify({"error": "Token não fornecido"}), 400

        # Aqui pegamos o body real que o SGP montou (com number e body da mensagem)
        body_real = request.get_json()

        # Fazemos o POST real pra API da Netbits
        response = requests.post(
            "https://chatapi.netbits.com.br/api/messages/send",
            headers={
                "Authorization": f"Bearer {sgp_token}",
                "Content-Type": "application/json"
            },
            json=body_real
        )

        # Retorna o que a API da Netbits responder
        return jsonify({
            "status_code": response.status_code,
            "response": response.json()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
