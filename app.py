from flask import Flask, render_template, request
from chatbot import greeting, response, sent_tokens

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
        return f"{BOT_NAME}: Bye! take care.."

    if user_message in ('thanks', 'thank you'):
        return f"{BOT_NAME}: You are welcome.."

    greeting_response = greeting(user_message)
    if greeting_response is not None:
        return f"{BOT_NAME}: {greeting_response}"

    bot_response = response(user_message)
    sent_tokens.remove(user_message)

    return f"{BOT_NAME}: {bot_response}"

if __name__ == '__main__':
    app.run(debug=True)