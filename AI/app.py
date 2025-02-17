from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# تحميل نموذج محادثة جاهز
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "يرجى إدخال رسالة."})

    response = chatbot(user_input)
    return jsonify({"response": response[0]["generated_text"]})

if __name__ == "__main__":
    app.run(debug=True)
