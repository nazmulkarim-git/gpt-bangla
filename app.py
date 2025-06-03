from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load OpenAI API key from environment or default
openai.api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

@app.route("/")
def index():
    return "✅ BanglaGPT Backend is running!"

@app.route("/api/message", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "তুমি একজন সহায়ক বাংলা সহচর। সংক্ষিপ্ত এবং প্রাঞ্জল ভাষায় উত্তর দাও।"},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        print("❌ OpenAI API Error:", e)
        return jsonify({"reply": "দুঃখিত, কিছু সমস্যা হয়েছে। পরে আবার চেষ্টা করুন।", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
