# CyberBot
CyberBot is a versatile AI designed to provide expert guidance on cybersecurity and online safety. With 50+ responses, it offers insights on phishing, malware, online account protection, and more. Stay secure online with CyberBot as your digital guardian.


Certainly, here's a complete set of code files for your CyberBot web application. You can copy and paste these files into your project directory.

**1. `cyberbot.py` (Your CyberBot logic):**

```python
# cyberbot.py
def cyberbot_response(user_input):
    # Your CyberBot logic here
    # Example: return "CyberBot: Hello! How can I assist you with cybersecurity and online safety today?"
```

**2. `templates/index.html` (HTML Template for Chat Interface):**

```html
<!DOCTYPE html>
<html>
<head>
    <title>CyberBot Chat</title>
</head>
<body>
    <h1>Welcome to CyberBot Chat</h1>
    <div id="chat-container">
        <!-- Chat messages will appear here -->
    </div>
    <input type="text" id="user-input" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button>

    <script>
        function addMessage(message, isUser) {
            const chatContainer = document.getElementById('chat-container');
            const messageDiv = document.createElement('div');
            messageDiv.className = isUser ? 'user-message' : 'bot-message';
            messageDiv.textContent = message;
            chatContainer.appendChild(messageDiv);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function sendMessage() {
            const userMessage = document.getElementById('user-input').value;
            addMessage(userMessage, true);

            fetch('/get_bot_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_input: userMessage }),
            })
                .then((response) => response.json())
                .then((data) => {
                    const botResponse = data.bot_response;
                    addMessage(botResponse, false);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });

            document.getElementById('user-input').value = '';
        }
    </script>
</body>
</html>
```

**3. `app.py` (Flask Application):**

```python
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
```

To use this code, follow these steps:

1. Create a directory for your project.

2. Create a Python file named `cyberbot.py` and define your CyberBot logic in it.

3. Create a `templates` directory within your project directory, and within it, create an HTML file named `index.html` with the provided HTML code.

4. Create a Python file named `app.py` and paste the Flask application code into it.

5. Install Flask by running `pip install Flask` in your terminal.

6. Run your Flask application by executing `python app.py` in your terminal.

Your CyberBot web application will be accessible at `http://localhost:5000`. Users can interact with it through the web interface you designed.

Remember to customize the CyberBot logic in `cyberbot.py` to handle user input and generate responses according to your requirements. You can also enhance the HTML template and JavaScript code in `index.html` to improve the chat interface and add more features.
