from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import traceback

app = Flask(__name__)
CORS(app)
openai.api_key = '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'  # OpenAI API anahtarınızı buraya yapıştırın

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Yeni API modelini kullanıyoruz
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ]
        )
        reply = response.choices[0].message['content'].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        print(traceback.format_exc())  # Hata mesajını yazdır
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)