# app.py
from flask import Flask, request, render_template, jsonify
from cyberbot import cyberbot_response  # Import your CyberBot logic function

app = Flask(__name__)

# Function to get a bot response
def get_bot_response(user_input):
    return cyberbot_response(user_input)

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define an API endpoint to get bot responses
@app.route('/get_bot_response', methods=['POST'])
def bot_response():
    user_input = request.json['user_input']
    bot_response = get_bot_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
