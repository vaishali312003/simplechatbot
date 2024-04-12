from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message'].lower()

    # Simple responses based on keywords
    if 'hello' in message:
        response = "Hi there!"
    elif 'how are you' in message:
        response = "I'm doing well, thank you!"
    elif 'bye' in message:
        response = "Goodbye! Take care."
    else:
        # If no keyword detected, return a random response
        responses = ["I'm not sure I understand.", "Could you please rephrase that?", "Sorry, I didn't get that."]
        response = random.choice(responses)

    return jsonify({'message': response})
