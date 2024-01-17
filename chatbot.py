# Importing the necessary libraries
import io
import random
import string # to process standard python strings
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')         # Download the punkt resource
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')


# Constants
BOT_NAME = "Unibuddy"
USER_PROMPT = "Your message here: "

# Reading the body of the messages
with open('q&a.txt', 'r', errors='ignore') as f:
    raw = f.read()

# Tokenization
sent_tokens = nltk.sent_tokenize(raw)   # converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)   # converts to list of words

# Preprocessing - Tokenization, lemmatization, and punctuation removal in the dataset

lemmer = nltk.stem.WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmer.lemmatize(token) for token in tokens]
    tokens = [token for token in tokens if token not in string.punctuation]
    return tokens


# Keyword matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generate a response based on user input
def response(user_response):
    response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=preprocess_text, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        response=response+"I am sorry! I don't understand you"
        return response
    else:
        response = response+sent_tokens[idx]
        return response


# Bot welcome and goodbye message
flag = True
print(f"{BOT_NAME}: Hello! Welcome to {BOT_NAME} - Your go-to companion for all things related to the school!")

while flag:
    user_response = input(USER_PROMPT).lower()

    if user_response != 'bye':
        if user_response in ('thanks', 'thank you'):
            flag = False
            print(f"{BOT_NAME}: You are welcome..")
        else:
            if greeting(user_response) is not None:
                print(f"{BOT_NAME}: {greeting(user_response)}")
            else:
                print(f"{BOT_NAME}: {response(user_response)}")
                sent_tokens.remove(user_response)
    else:
        flag = False
        print(f"{BOT_NAME}: Bye! take care..")

