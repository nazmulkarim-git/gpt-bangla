
from flask import Flask, request, jsonify, send_from_directory
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

openai.api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

@app.route("/")
def index():
    return "BanglaGPT Backend Running"

@app.route("/api/message", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150,
            temperature=0.7
        )
        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "দুঃখিত, কিছু সমস্যা হয়েছে। পরে আবার চেষ্টা করুন।", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
