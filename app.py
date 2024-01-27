from flask import Flask, render_template, request
from chatbot import chatbot  # Import the chatbot instance from chatbot.py
from chatterbot.conversation import Statement  # Import Statement for response processing

app = Flask(__name__)

# Constants
BOT_NAME = "Unibuddy"

@app.route('/')
def index():
    return render_template('index.html', bot_name=BOT_NAME)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message'].lower()

    if user_message == 'bye':
        return f"Bye! take care.."

    if user_message in ('thanks', 'thank you'):
        return f"You are welcome.."

    response = chatbot.get_response(Statement(text=user_message))

    # Remove the bot's name from the response
    response_text = str(response)
    response_text = response_text.replace(chatbot.name, '').strip()

    return f"{response_text}"

if __name__ == '__main__':
    app.run(debug=True)
