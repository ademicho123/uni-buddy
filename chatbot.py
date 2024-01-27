from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.logic import BestMatch

# Create the ChatBot instance
chatbot = ChatBot(
    'UniBuddy',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            'response_selection_method': 'chatterbot.response_selection.get_random_response',
            'default_response': 'I am still learning, but I am always improving.',
            'maximum_similarity_threshold': 0.80
        }
    ]
)

# Load Q&A data from text file
file_path = 'q&a.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    custom_data = [tuple(line.strip().split('|')) for line in file.readlines()]

# Train with both ListTrainer and ChatterBotCorpusTrainer
list_trainer = ListTrainer(chatbot)
list_trainer.train(custom_data)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train(
    'chatterbot.corpus.english'  # Optional: Add other corpora for general conversation
)

# Chatbot ready for response
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)
